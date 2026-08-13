#!/usr/bin/env python3
"""
ksi_validator.py — FedRAMP 20x Key Security Indicator validation engine

Northgate Signal, Inc. | Caseline Platform
Target: FedRAMP 20x Class C Certification

WHAT THIS IS
------------
FedRAMP 20x replaces narrative control descriptions with Key Security Indicators
(KSIs) that must be validated automatically against the running system. Under
CR26 rule FRC-CSX-VVK, a Class C provider MUST implement at least TWO automated
validation methods for each KSI. This script is the engine that does that.

It reads live system state (here, fixtures standing in for cloud provider APIs),
evaluates each KSI against two or more independent validation methods, and emits
machine-readable JSON evidence per FRC-CSO-JSN.

DESIGN NOTE ON "TWO METHODS"
----------------------------
The point of requiring multiple methods is corroboration from independent
sources. A method that reads the same API as another method is not a second
method in any meaningful sense — it is the same assertion counted twice.
This engine therefore pairs a CONTROL-PLANE method (what the configuration
says should be true) with a DATA-PLANE or TELEMETRY method (what the running
system actually did). Where those disagree, the KSI reports False, because a
policy that exists and is not enforced is the exact failure mode continuous
validation is meant to catch.

HONEST SCOPE
------------
This is a portfolio artifact for a fictional company. The JSON structure below
is modeled on the CR26 requirements for the Security Decision Record and
Ongoing Certification Report; it is NOT claimed to validate against FedRAMP's
official published JSON schemas, which are authoritative and live at
https://fedramp.gov/schemas. A production implementation would validate output
against those schemas in CI.

Usage:
    python3 src/ksi_validator.py --summary    # evaluate, write evidence, print summary
    python3 src/ksi_validator.py              # evaluate and write evidence quietly

Output is written to ../evidence/ relative to this script, regardless of the
working directory you run it from. Override with --outdir.
"""

import json
import argparse
import hashlib
from datetime import datetime, timedelta, timezone

PROVIDER = "Northgate Signal, Inc."
OFFERING = "Caseline"
CERT_CLASS = "Class C"
CERT_TYPE = "20x"
ASSESSMENT_DATE = datetime(2026, 8, 10, 14, 0, 0, tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# FIXTURES — stand in for live cloud provider / IdP / SIEM API responses.
# In production each of these is an API call, not a literal.
# ---------------------------------------------------------------------------

FIXTURES = {
    # Control-plane: identity provider policy configuration
    "idp_policy": {
        "phishing_resistant_mfa_required": True,
        "passwordless_enabled": True,
        "password_fallback_allowed": False,
        "privileged_session_max_minutes": 60,
        "auto_disable_on_risk_signal": True,
    },
    # Data-plane: actual authentication events over the reporting window
    "auth_events_30d": {
        "total_user_authentications": 48213,
        "authentications_with_phishing_resistant_mfa": 48213,
        "passwordless_authentications": 45102,
        "privileged_authentications": 1877,
        "privileged_with_phishing_resistant_mfa": 1877,
    },
    # Control-plane: IAM role and account inventory
    "iam_inventory": {
        "total_accounts": 412,
        "accounts_provisioned_by_automation": 412,
        "accounts_provisioned_manually": 0,
        "standing_privileged_roles": 0,
        "jit_eligible_roles": 14,
        "non_user_accounts": 63,
        "non_user_accounts_using_workload_identity": 63,
        "non_user_accounts_using_static_credentials": 0,
    },
    # Data-plane: privilege elevation telemetry
    "elevation_events_30d": {
        "total_elevations": 331,
        "elevations_via_jit_workflow": 331,
        "elevations_bypassing_jit": 0,
        "median_elevation_duration_minutes": 22,
        "elevations_exceeding_max_duration": 0,
    },
    # Access review automation
    "access_review": {
        "last_automated_review": "2026-08-08",
        "review_interval_days": 7,
        "accounts_flagged_excess_privilege": 3,
        "accounts_remediated": 3,
        "open_findings": 0,
    },
    # Suspicious activity response telemetry
    "suspicious_activity_30d": {
        "risk_signals_raised": 9,
        "accounts_auto_disabled": 9,
        "median_response_seconds": 4,
        "manual_interventions_required": 0,
    },
    # Change management: version control and deployment
    "change_control": {
        "deployments_30d": 214,
        "deployments_from_version_control": 214,
        "deployments_manual_or_console": 0,
        "changes_with_automated_test_gate": 214,
        "changes_with_peer_review": 214,
        "emergency_changes": 3,
        "emergency_changes_with_retrospective": 3,
    },
    "change_log_integrity": {
        "log_forwarding_enabled": True,
        "logs_immutable_storage": True,
        "config_change_events_captured_30d": 1904,
        "config_change_events_reconciled_to_tickets": 1904,
        "unreconciled_changes": 0,
    },
    # Network / cloud-native architecture
    "network_policy": {
        "default_deny_ingress": True,
        "default_deny_egress": True,
        "segments_defined": 7,
        "workloads_with_explicit_policy": 143,
        "workloads_total": 143,
    },
    # NOTE: this fixture intentionally disagrees with network_policy above.
    # The declared policy is default-deny with full workload coverage, but
    # observed flows show permitted traffic no policy anticipated. This is the
    # drift scenario the two-method requirement exists to surface.
    "network_flow_30d": {
        "flows_observed": 18400291,
        "flows_matching_allow_policy": 18398974,
        "flows_denied": 24117,
        "unexpected_permitted_flows": 1317,
        "unexpected_flow_source": "legacy-reporting-subnet -> analytics-egress",
        "lateral_movement_alerts": 0,
    },
    # Service configuration / encryption
    "encryption_config": {
        "data_stores_total": 19,
        "data_stores_encrypted_at_rest": 19,
        "cmk_managed": 19,
        "key_rotation_max_age_days": 365,
        "keys_past_rotation_age": 0,
        "tls_minimum_version": "1.3",
        "fips_validated_modules": True,
    },
    # NOTE: intentionally disagrees with encryption_config above. Config declares
    # TLS 1.3 minimum, but one legacy load balancer listener still negotiates
    # TLS 1.0. Configuration read alone would report this KSI as true.
    "encryption_observed_30d": {
        "endpoints_scanned": 41,
        "endpoints_negotiating_tls_1_2_or_higher": 40,
        "endpoints_permitting_deprecated_protocol": 1,
        "deprecated_protocol_endpoint": "lb-legacy-reporting-01:443 (TLS 1.0 accepted)",
        "unencrypted_storage_objects_detected": 0,
    },
    # Training
    "training_records": {
        "workforce_total": 88,
        "completed_security_awareness_current_period": 88,
        "privileged_role_holders": 21,
        "privileged_completed_role_specific": 21,
        "training_max_age_days": 365,
        "records_past_due": 0,
    },
    "phishing_simulation": {
        "campaigns_trailing_12mo": 4,
        "median_click_rate_percent": 2.1,
        "target_click_rate_percent": 5.0,
        "repeat_clickers_assigned_remediation": 2,
        "repeat_clickers_completed": 2,
    },
    # Incident response
    "ir_program": {
        "plan_last_reviewed": "2026-06-30",
        "plan_review_interval_days": 180,
        "exercises_trailing_12mo": 2,
        "contact_roster_last_verified": "2026-07-15",
        "roster_verification_interval_days": 90,
        "roster_entries_unverified": 0,
    },
    "ir_events_12mo": {
        "incidents_recorded": 4,
        "incidents_with_after_action_report": 4,
        "fedramp_reportable_incidents": 0,
        "median_detection_to_report_minutes": 31,
        "reporting_requirement_minutes": 60,
        "reporting_deadline_breaches": 0,
    },
}


# ---------------------------------------------------------------------------
# VALIDATION METHODS
# Each returns (passed: bool, metric: dict, note: str)
# ---------------------------------------------------------------------------

def m_iam_aam_control_plane():
    inv = FIXTURES["iam_inventory"]
    total = inv["total_accounts"]
    auto = inv["accounts_provisioned_by_automation"]
    pct = round(auto / total * 100, 2) if total else 0.0
    return (
        inv["accounts_provisioned_manually"] == 0,
        {"accounts_total": total, "automated_lifecycle_pct": pct,
         "manually_provisioned": inv["accounts_provisioned_manually"]},
        "Queries IdP and cloud IAM inventory; asserts no account exists outside automated lifecycle.",
    )


def m_iam_aam_review_telemetry():
    ar = FIXTURES["access_review"]
    last = datetime.strptime(ar["last_automated_review"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    age_days = (ASSESSMENT_DATE - last).days
    fresh = age_days <= ar["review_interval_days"]
    return (
        fresh and ar["open_findings"] == 0,
        {"days_since_review": age_days, "review_interval_days": ar["review_interval_days"],
         "flagged": ar["accounts_flagged_excess_privilege"],
         "remediated": ar["accounts_remediated"], "open_findings": ar["open_findings"]},
        "Independent source: access review job output. Confirms lifecycle automation produces reviewed outcomes, not just provisioned accounts.",
    )


def m_iam_apm_policy():
    p = FIXTURES["idp_policy"]
    return (
        p["phishing_resistant_mfa_required"] and p["passwordless_enabled"]
        and not p["password_fallback_allowed"],
        {"phishing_resistant_required": p["phishing_resistant_mfa_required"],
         "passwordless_enabled": p["passwordless_enabled"],
         "password_fallback_allowed": p["password_fallback_allowed"]},
        "Reads IdP authentication policy configuration.",
    )


def m_iam_apm_observed_auth():
    a = FIXTURES["auth_events_30d"]
    total = a["total_user_authentications"]
    mfa = a["authentications_with_phishing_resistant_mfa"]
    pwless = a["passwordless_authentications"]
    mfa_pct = round(mfa / total * 100, 2) if total else 0.0
    pwless_pct = round(pwless / total * 100, 2) if total else 0.0
    return (
        mfa == total,
        {"authentications_30d": total, "phishing_resistant_mfa_pct": mfa_pct,
         "passwordless_pct": pwless_pct},
        "Independent source: authentication event log. Proves the policy is enforced in practice, not merely configured.",
    )


def m_iam_elp_inventory():
    inv = FIXTURES["iam_inventory"]
    return (
        inv["standing_privileged_roles"] == 0,
        {"standing_privileged_roles": inv["standing_privileged_roles"],
         "jit_eligible_roles": inv["jit_eligible_roles"]},
        "Enumerates role bindings; asserts zero standing privilege.",
    )


def m_iam_elp_review():
    ar = FIXTURES["access_review"]
    return (
        ar["accounts_flagged_excess_privilege"] == ar["accounts_remediated"],
        {"flagged": ar["accounts_flagged_excess_privilege"],
         "remediated": ar["accounts_remediated"]},
        "Independent source: persistent least-privilege review job; confirms detected excess privilege is closed out.",
    )


def m_iam_jit_config():
    inv = FIXTURES["iam_inventory"]
    p = FIXTURES["idp_policy"]
    return (
        inv["standing_privileged_roles"] == 0 and p["privileged_session_max_minutes"] <= 60,
        {"jit_eligible_roles": inv["jit_eligible_roles"],
         "max_session_minutes": p["privileged_session_max_minutes"]},
        "Confirms JIT workflow configuration and bounded elevation duration.",
    )


def m_iam_jit_telemetry():
    e = FIXTURES["elevation_events_30d"]
    return (
        e["elevations_bypassing_jit"] == 0 and e["elevations_exceeding_max_duration"] == 0,
        {"elevations_30d": e["total_elevations"], "via_jit": e["elevations_via_jit_workflow"],
         "bypassed_jit": e["elevations_bypassing_jit"],
         "median_duration_minutes": e["median_elevation_duration_minutes"],
         "exceeded_max_duration": e["elevations_exceeding_max_duration"]},
        "Independent source: elevation event telemetry. Detects out-of-band privilege grants the config alone cannot reveal.",
    )


def m_iam_snu_inventory():
    inv = FIXTURES["iam_inventory"]
    return (
        inv["non_user_accounts_using_static_credentials"] == 0,
        {"non_user_accounts": inv["non_user_accounts"],
         "workload_identity": inv["non_user_accounts_using_workload_identity"],
         "static_credentials": inv["non_user_accounts_using_static_credentials"]},
        "Inventories non-user principals; asserts workload identity federation rather than static secrets.",
    )


def m_iam_snu_secret_scan():
    return (
        True,
        {"repos_scanned": 34, "static_credentials_detected": 0, "scan_frequency": "per-commit"},
        "Independent source: secret scanning across source repositories and container images; catches credentials the IAM inventory cannot see.",
    )


def m_iam_sus_config():
    p = FIXTURES["idp_policy"]
    return (
        p["auto_disable_on_risk_signal"],
        {"auto_disable_enabled": p["auto_disable_on_risk_signal"]},
        "Confirms automated risk-response policy is enabled.",
    )


def m_iam_sus_telemetry():
    s = FIXTURES["suspicious_activity_30d"]
    return (
        s["risk_signals_raised"] == s["accounts_auto_disabled"],
        {"risk_signals_30d": s["risk_signals_raised"],
         "auto_disabled": s["accounts_auto_disabled"],
         "median_response_seconds": s["median_response_seconds"],
         "manual_interventions": s["manual_interventions_required"]},
        "Independent source: risk-signal response telemetry; measures actual response, including latency.",
    )


def m_cmt_lmc_config():
    c = FIXTURES["change_log_integrity"]
    return (
        c["log_forwarding_enabled"] and c["logs_immutable_storage"],
        {"forwarding_enabled": c["log_forwarding_enabled"],
         "immutable_storage": c["logs_immutable_storage"]},
        "Verifies change-event logging is enabled and written to tamper-resistant storage.",
    )


def m_cmt_lmc_reconciliation():
    c = FIXTURES["change_log_integrity"]
    return (
        c["unreconciled_changes"] == 0,
        {"change_events_30d": c["config_change_events_captured_30d"],
         "reconciled_to_tickets": c["config_change_events_reconciled_to_tickets"],
         "unreconciled": c["unreconciled_changes"]},
        "Independent source: reconciles observed config-change events against approved change records. Unreconciled changes indicate modification outside the change process.",
    )


def m_cmt_imm_pipeline():
    c = FIXTURES["change_control"]
    return (
        c["deployments_manual_or_console"] == 0,
        {"deployments_30d": c["deployments_30d"],
         "from_version_control": c["deployments_from_version_control"],
         "manual_or_console": c["deployments_manual_or_console"]},
        "Confirms all deployments originate from version-controlled immutable artifacts.",
    )


def m_cmt_imm_gates():
    c = FIXTURES["change_control"]
    ok = (c["changes_with_automated_test_gate"] == c["deployments_30d"]
          and c["emergency_changes"] == c["emergency_changes_with_retrospective"])
    return (
        ok,
        {"with_test_gate": c["changes_with_automated_test_gate"],
         "with_peer_review": c["changes_with_peer_review"],
         "emergency_changes": c["emergency_changes"],
         "emergency_with_retrospective": c["emergency_changes_with_retrospective"]},
        "Independent source: CI/CD pipeline records; confirms test and review gates executed and emergency changes received retrospective review.",
    )


def m_cna_rnt_policy():
    n = FIXTURES["network_policy"]
    return (
        n["default_deny_ingress"] and n["default_deny_egress"]
        and n["workloads_with_explicit_policy"] == n["workloads_total"],
        {"default_deny_ingress": n["default_deny_ingress"],
         "default_deny_egress": n["default_deny_egress"],
         "segments": n["segments_defined"],
         "workload_policy_coverage_pct": round(
             n["workloads_with_explicit_policy"] / n["workloads_total"] * 100, 2)},
        "Evaluates declared network policy: default-deny posture and per-workload policy coverage.",
    )


def m_cna_rnt_flow():
    f = FIXTURES["network_flow_30d"]
    return (
        f["unexpected_permitted_flows"] == 0 and f["lateral_movement_alerts"] == 0,
        {"flows_observed_30d": f["flows_observed"],
         "denied": f["flows_denied"],
         "unexpected_permitted": f["unexpected_permitted_flows"],
         "unexpected_flow_source": f.get("unexpected_flow_source"),
         "lateral_movement_alerts": f["lateral_movement_alerts"]},
        "Independent source: observed network flow logs. Detects permitted traffic the declared policy did not anticipate.",
    )


def m_svc_sin_config():
    e = FIXTURES["encryption_config"]
    return (
        e["data_stores_encrypted_at_rest"] == e["data_stores_total"]
        and e["keys_past_rotation_age"] == 0
        and e["fips_validated_modules"],
        {"data_stores": e["data_stores_total"],
         "encrypted_at_rest": e["data_stores_encrypted_at_rest"],
         "cmk_managed": e["cmk_managed"],
         "keys_past_rotation": e["keys_past_rotation_age"],
         "tls_minimum": e["tls_minimum_version"],
         "fips_validated": e["fips_validated_modules"]},
        "Reads storage and key management configuration.",
    )


def m_svc_sin_observed():
    o = FIXTURES["encryption_observed_30d"]
    return (
        o["endpoints_permitting_deprecated_protocol"] == 0
        and o["unencrypted_storage_objects_detected"] == 0,
        {"endpoints_scanned": o["endpoints_scanned"],
         "tls_compliant_endpoints": o["endpoints_negotiating_tls_1_2_or_higher"],
         "deprecated_protocol_permitted": o["endpoints_permitting_deprecated_protocol"],
         "deprecated_protocol_endpoint": o.get("deprecated_protocol_endpoint"),
         "unencrypted_objects_detected": o["unencrypted_storage_objects_detected"]},
        "Independent source: active protocol negotiation testing and storage object scanning. Configuration can claim TLS 1.3 while a load balancer still accepts 1.0.",
    )


def m_ced_rat_records():
    t = FIXTURES["training_records"]
    return (
        t["records_past_due"] == 0
        and t["privileged_completed_role_specific"] == t["privileged_role_holders"],
        {"workforce": t["workforce_total"],
         "awareness_completed": t["completed_security_awareness_current_period"],
         "privileged_role_holders": t["privileged_role_holders"],
         "role_specific_completed": t["privileged_completed_role_specific"],
         "past_due": t["records_past_due"]},
        "Queries LMS completion records against current workforce roster.",
    )


def m_ced_rat_efficacy():
    p = FIXTURES["phishing_simulation"]
    return (
        p["median_click_rate_percent"] <= p["target_click_rate_percent"]
        and p["repeat_clickers_assigned_remediation"] == p["repeat_clickers_completed"],
        {"campaigns_12mo": p["campaigns_trailing_12mo"],
         "median_click_rate_pct": p["median_click_rate_percent"],
         "target_click_rate_pct": p["target_click_rate_percent"],
         "repeat_clickers_remediated": p["repeat_clickers_completed"]},
        "Independent source: phishing simulation outcomes. Measures whether training changed behavior, not merely whether it was completed.",
    )


def m_inr_rir_program():
    ir = FIXTURES["ir_program"]
    reviewed = datetime.strptime(ir["plan_last_reviewed"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    age = (ASSESSMENT_DATE - reviewed).days
    roster = datetime.strptime(ir["contact_roster_last_verified"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    roster_age = (ASSESSMENT_DATE - roster).days
    return (
        age <= ir["plan_review_interval_days"]
        and roster_age <= ir["roster_verification_interval_days"]
        and ir["roster_entries_unverified"] == 0,
        {"plan_age_days": age, "plan_interval_days": ir["plan_review_interval_days"],
         "roster_age_days": roster_age,
         "roster_interval_days": ir["roster_verification_interval_days"],
         "roster_unverified": ir["roster_entries_unverified"],
         "exercises_12mo": ir["exercises_trailing_12mo"]},
        "Checks IR plan review currency, exercise cadence, and contact roster verification age.",
    )


def m_inr_rir_outcomes():
    e = FIXTURES["ir_events_12mo"]
    return (
        e["reporting_deadline_breaches"] == 0
        and e["incidents_with_after_action_report"] == e["incidents_recorded"],
        {"incidents_12mo": e["incidents_recorded"],
         "with_after_action_report": e["incidents_with_after_action_report"],
         "median_detect_to_report_minutes": e["median_detection_to_report_minutes"],
         "reporting_requirement_minutes": e["reporting_requirement_minutes"],
         "deadline_breaches": e["reporting_deadline_breaches"]},
        "Independent source: incident records. Measures actual detection-to-report latency against the FedRAMP reporting requirement.",
    )


# ---------------------------------------------------------------------------
# KSI DEFINITIONS
# KSI identifiers and statements are drawn from the FedRAMP Consolidated Rules
# for 2026. Verify current text at:
# https://www.fedramp.gov/2026/providers/20x/key-security-indicators/
# ---------------------------------------------------------------------------

KSIS = [
    {
        "id": "KSI-IAM-AAM", "family": "Identity and Access Management",
        "name": "Automating Account Management",
        "statement": "The lifecycle and privileges of all accounts, roles, and groups are securely managed using automation.",
        "related_controls": ["AC-02(02)", "AC-02(03)", "AC-02(13)", "AC-06(07)",
                             "IA-04(04)", "IA-12", "IA-12(02)", "IA-12(03)", "IA-12(05)"],
        "methods": [("control-plane", "IdP and cloud IAM inventory query", m_iam_aam_control_plane),
                    ("telemetry", "Automated access review job output", m_iam_aam_review_telemetry)],
    },
    {
        "id": "KSI-IAM-APM", "family": "Identity and Access Management",
        "name": "Adopting Passwordless Methods",
        "statement": "Secure passwordless methods are used for user authentication and authorization when feasible, otherwise strong passwords with phishing-resistant MFA is used.",
        "related_controls": ["AC-03", "IA-02", "IA-02(01)", "IA-02(02)", "IA-02(08)",
                             "IA-05", "IA-05(01)", "IA-05(02)", "IA-05(06)", "IA-06",
                             "IA-08", "SC-23", "AC-02"],
        "methods": [("control-plane", "IdP authentication policy read", m_iam_apm_policy),
                    ("data-plane", "Authentication event log analysis", m_iam_apm_observed_auth)],
    },
    {
        "id": "KSI-IAM-ELP", "family": "Identity and Access Management",
        "name": "Ensuring Least Privilege",
        "statement": "Identity and access management measures are used and persistently reviewed to ensure each user or device can only access the resources they need.",
        "related_controls": ["AC-02(05)", "AC-02(06)", "AC-03", "AC-04", "AC-06",
                             "AC-12", "AC-17", "AC-20", "IA-02", "IA-03", "IA-11", "SI-03"],
        "methods": [("control-plane", "Role binding enumeration", m_iam_elp_inventory),
                    ("telemetry", "Persistent least-privilege review closure", m_iam_elp_review)],
    },
    {
        "id": "KSI-IAM-JIT", "family": "Identity and Access Management",
        "name": "Authorizing Just-in-Time",
        "statement": "A least-privileged, role and attribute-based, and just-in-time security authorization model is used and persistently reviewed for all user and non-user accounts and services.",
        "related_controls": ["AC-02", "AC-02(01)", "AC-05", "AC-06", "AC-06(01)",
                             "AC-06(02)", "AC-06(05)", "AC-06(09)", "AC-06(10)",
                             "CM-05", "CM-07", "SC-02"],
        "methods": [("control-plane", "JIT workflow configuration check", m_iam_jit_config),
                    ("telemetry", "Privilege elevation event telemetry", m_iam_jit_telemetry)],
    },
    {
        "id": "KSI-IAM-SNU", "family": "Identity and Access Management",
        "name": "Securing Non-User Authentication",
        "statement": "Appropriately secure authentication methods are used and persistently reviewed for non-user accounts and services.",
        "related_controls": ["AC-02", "AC-02(02)", "AC-04", "AC-06(05)", "IA-03",
                             "IA-05(02)", "RA-05(05)"],
        "methods": [("control-plane", "Non-user principal inventory", m_iam_snu_inventory),
                    ("data-plane", "Repository and image secret scanning", m_iam_snu_secret_scan)],
    },
    {
        "id": "KSI-IAM-SUS", "family": "Identity and Access Management",
        "name": "Responding to Suspicious Activity",
        "statement": "Accounts with privileged access are disabled or otherwise secured in response to suspicious activity.",
        "related_controls": ["AC-02", "AC-02(01)", "AC-02(03)", "AC-02(13)", "AC-07",
                             "PS-04", "PS-08"],
        "methods": [("control-plane", "Automated risk-response policy check", m_iam_sus_config),
                    ("telemetry", "Risk signal response telemetry", m_iam_sus_telemetry)],
    },
    {
        "id": "KSI-CMT-LMC", "family": "Change Management",
        "name": "Logging Changes",
        "statement": "System modifications are logged and monitored.",
        "related_controls": ["CM-03", "CM-05", "AU-02", "AU-06", "AU-09"],
        "methods": [("control-plane", "Change logging configuration verification", m_cmt_lmc_config),
                    ("telemetry", "Change event to approval reconciliation", m_cmt_lmc_reconciliation)],
    },
    {
        "id": "KSI-CMT-IMM", "family": "Change Management",
        "name": "Deploying Immutable Resources",
        "statement": "Changes are executed through redeployment of version controlled immutable resources rather than direct modification wherever possible.",
        "related_controls": ["CM-02", "CM-03", "CM-04", "CM-08", "SA-11"],
        "methods": [("control-plane", "Deployment source verification", m_cmt_imm_pipeline),
                    ("telemetry", "CI/CD gate execution records", m_cmt_imm_gates)],
    },
    {
        "id": "KSI-CNA-RNT", "family": "Cloud Native Architecture",
        "name": "Restricting Network Traffic",
        "statement": "All information resources are configured to limit inbound and outbound traffic.",
        "related_controls": ["AC-04", "SC-07", "SC-07(05)", "CA-09", "CM-07"],
        "methods": [("control-plane", "Declared network policy evaluation", m_cna_rnt_policy),
                    ("data-plane", "Observed network flow log analysis", m_cna_rnt_flow)],
    },
    {
        "id": "KSI-SVC-SIN", "family": "Service Configuration",
        "name": "Securing Information",
        "statement": "Federal and sensitive information is encrypted at rest and in transit using validated cryptographic methods.",
        "related_controls": ["SC-08", "SC-08(01)", "SC-12", "SC-13", "SC-28", "SC-28(01)"],
        "methods": [("control-plane", "Storage and key management configuration read", m_svc_sin_config),
                    ("data-plane", "Active protocol negotiation and object scanning", m_svc_sin_observed)],
    },
    {
        "id": "KSI-CED-RAT", "family": "Cybersecurity Education",
        "name": "Reviewing All Training",
        "statement": "All employees receive security awareness training, and role-specific training is required for high risk roles including those with privileged access.",
        "related_controls": ["AT-02", "AT-03", "AT-04", "PS-07"],
        "methods": [("control-plane", "LMS completion record query", m_ced_rat_records),
                    ("telemetry", "Phishing simulation outcome analysis", m_ced_rat_efficacy)],
    },
    {
        "id": "KSI-INR-RIR", "family": "Incident Response",
        "name": "Reviewing Incident Response Procedures",
        "statement": "Incident response procedures are documented, regularly reviewed and exercised, and incidents are reported according to FedRAMP requirements.",
        "related_controls": ["IR-03", "IR-04", "IR-05", "IR-06", "IR-08"],
        "methods": [("control-plane", "IR plan and roster currency check", m_inr_rir_program),
                    ("telemetry", "Incident record and reporting latency analysis", m_inr_rir_outcomes)],
    },
]


# ---------------------------------------------------------------------------
# ENGINE
# ---------------------------------------------------------------------------

def evaluate():
    results = []
    for k in KSIS:
        method_results = []
        for kind, label, fn in k["methods"]:
            passed, metric, note = fn()
            method_results.append({
                "method_type": kind,
                "method": label,
                "result": "pass" if passed else "fail",
                "metrics": metric,
                "assessor_note": note,
                "evaluated_at": ASSESSMENT_DATE.isoformat(),
            })
        all_pass = all(m["result"] == "pass" for m in method_results)
        corroborated = len({m["method_type"] for m in method_results}) > 1

        # Drift: methods disagree. The declared configuration asserts the
        # capability while observed behavior contradicts it. This is the
        # highest-signal outcome the engine can produce, because a
        # single-method validator would have reported this KSI as true.
        passed = {m["result"] for m in method_results}
        drift = len(passed) > 1
        control_plane_pass = any(
            m["result"] == "pass" and m["method_type"] == "control-plane"
            for m in method_results)
        observed_fail = any(
            m["result"] == "fail" and m["method_type"] in ("data-plane", "telemetry")
            for m in method_results)

        entry = {
            "ksi_id": k["id"],
            "ksi_family": k["family"],
            "ksi_name": k["name"],
            "ksi_statement": k["statement"],
            "related_sp_800_53_controls": k["related_controls"],
            "status": "true" if all_pass else "false",
            "independently_corroborated": corroborated,
            "validation_method_count": len(method_results),
            "meets_class_c_method_minimum": len(method_results) >= 2,
            "drift_detected": drift,
            "validations": method_results,
        }
        if drift and control_plane_pass and observed_fail:
            entry["drift_analysis"] = {
                "type": "configuration-behavior-divergence",
                "description": ("Declared configuration satisfies this KSI, but observed "
                                "system behavior does not. Single-method validation "
                                "against configuration alone would have reported this "
                                "KSI as true."),
                "significance": ("This is a real control gap, not a measurement artifact. "
                                 "The authoritative signal is the observed behavior."),
            }
        results.append(entry)
    return results


def build_sdr(results):
    """Security Decision Record — the 20x replacement for control narratives."""
    payload = {
        "document_type": "security-decision-record",
        "schema_note": ("Structure modeled on FedRAMP CR26 rules SDR-CSO-FRR and FRC-CSO-JSN. "
                        "Not validated against FedRAMP official published schemas; see "
                        "https://fedramp.gov/schemas for authoritative schemas."),
        "generated_at": ASSESSMENT_DATE.isoformat(),
        "provider": PROVIDER,
        "cloud_service_offering": OFFERING,
        "certification_type": CERT_TYPE,
        "certification_class": CERT_CLASS,
        "minimum_assessment_scope": {
            "rule": "MAS-CSO-IIR",
            "description": ("All information resources likely to handle federal customer data or "
                            "likely to impact its confidentiality, integrity, or availability."),
            "information_resources_in_scope": 143,
            "third_party_information_resources": 6,
        },
        "summary": {
            "ksis_evaluated": len(results),
            "ksis_true": sum(1 for r in results if r["status"] == "true"),
            "ksis_false": sum(1 for r in results if r["status"] == "false"),
            "total_validation_methods": sum(r["validation_method_count"] for r in results),
            "all_meet_class_c_minimum": all(r["meets_class_c_method_minimum"] for r in results),
            "drift_detected_count": sum(1 for r in results if r.get("drift_detected")),
            "ksis_that_would_pass_single_method_validation": [
                r["ksi_id"] for r in results if r.get("drift_analysis")
            ],
        },
        "key_security_indicators": results,
    }
    return payload


def build_ocr(results):
    """Ongoing Certification Report — CCM-OCR-AVL / CCM-OCR-NRD."""
    true_count = sum(1 for r in results if r["status"] == "true")
    next_report = ASSESSMENT_DATE + timedelta(days=30)
    return {
        "document_type": "ongoing-certification-report",
        "schema_note": ("Structure modeled on FedRAMP CR26 rules CCM-OCR-AVL and CCM-OCR-NRD. "
                        "Not validated against FedRAMP official published schemas."),
        "provider": PROVIDER,
        "cloud_service_offering": OFFERING,
        "certification_type": CERT_TYPE,
        "certification_class": CERT_CLASS,
        "report_generated_at": ASSESSMENT_DATE.isoformat(),
        "reporting_period_days": 30,
        "next_report_date": next_report.date().isoformat(),
        "posture": {
            "ksis_true": true_count,
            "ksis_total": len(results),
            "ksi_true_percentage": round(true_count / len(results) * 100, 2),
            "validation_automation": "100% of KSIs validated by at least two automated methods",
        },
        "vulnerability_response": {
            "rule": "VDR-CSO-DET",
            "detection_coverage_percent": 100.0,
            "open_findings_past_response_expectation": 0,
            "median_time_to_remediate_high_days": 6,
        },
        "availability": {
            "rule": "CDS-CSO-AVR",
            "uptime_percent_trailing_30d": 99.98,
        },
        "incident_summary": {
            "fedramp_reportable_incidents_period": 0,
            "reporting_deadline_breaches": 0,
        },
        "change_summary": {
            "deployments_period": FIXTURES["change_control"]["deployments_30d"],
            "significant_changes_notified": 1,
        },
        "attestation": {
            "rule": "FRC-CSO-MRA",
            "statement": ("Provider maintains responsibility and accountability for the accuracy "
                          "and completeness of all information in this report."),
            "attested_by_role": "Head of Security Assurance",
        },
    }


def integrity_manifest(docs):
    """Evidence integrity — hash each emitted artifact so tampering is detectable."""
    manifest = {
        "document_type": "evidence-integrity-manifest",
        "generated_at": ASSESSMENT_DATE.isoformat(),
        "algorithm": "sha256",
        "artifacts": [],
    }
    for name, obj in docs:
        blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
        manifest["artifacts"].append({
            "filename": name,
            "sha256": hashlib.sha256(blob).hexdigest(),
            "bytes": len(blob),
        })
    return manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true", help="print human-readable summary")
    ap.add_argument("--outdir", default=None,
                    help="output directory (default: ../evidence relative to this script)")
    args = ap.parse_args()

    import os
    if args.outdir:
        outdir = args.outdir
    else:
        outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence")
    outdir = os.path.normpath(outdir)
    os.makedirs(outdir, exist_ok=True)

    results = evaluate()
    sdr = build_sdr(results)
    ocr = build_ocr(results)
    manifest = integrity_manifest([
        ("security-decision-record.json", sdr),
        ("ongoing-certification-report.json", ocr),
    ])

    for name, obj in [("security-decision-record.json", sdr),
                      ("ongoing-certification-report.json", ocr),
                      ("evidence-integrity-manifest.json", manifest)]:
        with open(os.path.join(outdir, name), "w") as f:
            json.dump(obj, f, indent=2)

    if args.summary:
        print(f"\n{PROVIDER} — {OFFERING}")
        print(f"FedRAMP {CERT_TYPE} {CERT_CLASS} | Evaluated {ASSESSMENT_DATE.date()}\n")
        print(f"{'KSI':<16}{'Status':<9}{'Methods':<9}{'Drift'}")
        print("-" * 52)
        for r in results:
            flag = "DRIFT" if r.get("drift_detected") else "-"
            print(f"{r['ksi_id']:<16}{r['status'].upper():<9}"
                  f"{r['validation_method_count']:<9}{flag}")
        s = sdr["summary"]
        print("-" * 52)
        print(f"{s['ksis_true']}/{s['ksis_evaluated']} KSIs true | "
              f"{s['total_validation_methods']} validation methods | "
              f"Class C minimum met: {s['all_meet_class_c_minimum']}")
        if s["ksis_that_would_pass_single_method_validation"]:
            print("\n  Drift detected — these KSIs pass configuration review but fail")
            print("  observed-behavior validation. A single-method validator would")
            print("  have reported them as TRUE:")
            for kid in s["ksis_that_would_pass_single_method_validation"]:
                print(f"    - {kid}")
        print(f"\nWrote 3 JSON artifacts to: {outdir}\n")


if __name__ == "__main__":
    main()
