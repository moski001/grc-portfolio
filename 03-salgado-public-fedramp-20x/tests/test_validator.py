#!/usr/bin/env python3
"""
test_validator.py — regression tests for ksi_validator.py

These tests run the engine against its own authored fixtures. They show how the
implementation behaves under defined conditions. They are not an experiment and
say nothing about detection rates in a real environment.

    A  Configuration-only validation misses the two drift conditions.
    B  Two methods reading the same source still satisfy the method count,
       but are not reported as independently corroborated, whatever their
       labels say.
    C  Configuration plus independently sourced behavior detects drift, and
       the result follows the fixtures in both directions.
    D  The integrity check rejects an altered or missing evidence file.

Usage (standard library only):
    python3 -m unittest discover -s tests -v
"""

import contextlib
import io
import os
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))

import ksi_validator as v  # noqa: E402

EVIDENCE = os.path.join(HERE, "..", "evidence")
DRIFT_KSIS = ["KSI-CNA-RNT", "KSI-SVC-SIN"]


def by_id(results):
    return {r["ksi_id"]: r for r in results}


def control_plane_only():
    """The KSI set with every data-plane and telemetry method removed."""
    return [dict(k, methods=[m for m in k["methods"] if m[0] == "control-plane"])
            for k in v.KSIS]


def write_evidence(outdir):
    results = v.evaluate()
    blobs = [("security-decision-record.json", v.serialize(v.build_sdr(results))),
             ("ongoing-certification-report.json", v.serialize(v.build_ocr(results)))]
    blobs.append(("evidence-integrity-manifest.json",
                  v.serialize(v.integrity_manifest(blobs))))
    for name, blob in blobs:
        with open(os.path.join(outdir, name), "wb") as f:
            f.write(blob)
    return blobs


def run_verify(outdir):
    with contextlib.redirect_stdout(io.StringIO()):
        return v.verify(outdir)


class TestA_ConfigurationOnly(unittest.TestCase):

    def test_configuration_only_reports_every_ksi_true(self):
        with mock.patch.object(v, "KSIS", control_plane_only()):
            results = v.evaluate()
        self.assertEqual(len(results), 13)
        self.assertTrue(all(r["status"] == "true" for r in results))

    def test_configuration_only_misses_both_drift_conditions(self):
        with mock.patch.object(v, "KSIS", control_plane_only()):
            results = by_id(v.evaluate())
        for ksi in DRIFT_KSIS:
            self.assertEqual(results[ksi]["status"], "true")
            self.assertFalse(results[ksi]["drift_detected"])

    def test_configuration_only_fails_the_class_c_method_count(self):
        with mock.patch.object(v, "KSIS", control_plane_only()):
            results = v.evaluate()
        self.assertFalse(any(r["meets_class_c_method_minimum"] for r in results))


class TestB_SameSourceCountedTwice(unittest.TestCase):
    """KSI-CNA-RNT with its policy read run twice under two different labels."""

    def duplicated(self):
        ksis = []
        for k in v.KSIS:
            if k["id"] == "KSI-CNA-RNT":
                policy = next(m[2] for m in k["methods"] if m[0] == "control-plane")
                k = dict(k, methods=[
                    ("control-plane", "Declared network policy evaluation", policy),
                    ("data-plane", "Declared network policy evaluation (second read)", policy),
                ])
            ksis.append(k)
        return ksis

    def test_duplicate_source_satisfies_the_method_count_and_hides_drift(self):
        with mock.patch.object(v, "KSIS", self.duplicated()):
            r = by_id(v.evaluate())["KSI-CNA-RNT"]
        self.assertTrue(r["meets_class_c_method_minimum"])
        self.assertEqual(r["status"], "true")
        self.assertFalse(r["drift_detected"])

    def test_same_source_is_not_corroborated_despite_different_labels(self):
        with mock.patch.object(v, "KSIS", self.duplicated()):
            r = by_id(v.evaluate())["KSI-CNA-RNT"]
        self.assertEqual({m["method_type"] for m in r["validations"]},
                         {"control-plane", "data-plane"})
        self.assertFalse(r["independently_corroborated"])

    def test_method_that_reads_no_evidence_is_not_corroborated(self):
        constant = ("telemetry", "Always passes", lambda: (True, {}, "reads nothing"))
        ksis = [dict(k, methods=[k["methods"][0], constant]) if k["id"] == "KSI-IAM-APM" else k
                for k in v.KSIS]
        with mock.patch.object(v, "KSIS", ksis):
            r = by_id(v.evaluate())["KSI-IAM-APM"]
        self.assertFalse(r["independently_corroborated"])

    def test_baseline_names_the_ksis_whose_methods_share_a_source(self):
        shared = [r["ksi_id"] for r in v.evaluate() if not r["independently_corroborated"]]
        self.assertEqual(shared, ["KSI-CMT-LMC", "KSI-CMT-RMV"])

    def test_a_second_source_is_enough_even_when_one_is_shared(self):
        # KSI-PIY-GIV: discovery is reconciled against the inventory record,
        # so the second method reads both. Discovery is still new evidence.
        r = by_id(v.evaluate())["KSI-PIY-GIV"]
        self.assertTrue(r["independently_corroborated"])


class TestC_IndependentBehavioralEvidence(unittest.TestCase):

    def test_baseline_detects_exactly_the_two_drift_conditions(self):
        results = v.evaluate()
        drifted = [r["ksi_id"] for r in results if r.get("drift_analysis")]
        self.assertEqual(drifted, DRIFT_KSIS)
        self.assertEqual(sum(r["status"] == "true" for r in results), 11)
        self.assertEqual(sum(r["validation_method_count"] for r in results), 26)

    def test_removing_the_drift_from_the_fixtures_clears_the_findings(self):
        with mock.patch.dict(v.FIXTURES["network_flow_30d"],
                             {"unexpected_permitted_flows": 0}), \
             mock.patch.dict(v.FIXTURES["encryption_observed_30d"],
                             {"endpoints_permitting_deprecated_protocol": 0}):
            results = v.evaluate()
        self.assertTrue(all(r["status"] == "true" for r in results))
        self.assertFalse(any(r["drift_detected"] for r in results))

    def test_new_drift_in_a_passing_ksi_is_detected(self):
        with mock.patch.dict(v.FIXTURES["elevation_events_30d"],
                             {"elevations_bypassing_jit": 1}):
            r = by_id(v.evaluate())["KSI-IAM-JIT"]
        self.assertEqual(r["status"], "false")
        self.assertTrue(r["drift_detected"])
        self.assertIn("drift_analysis", r)

    def test_one_unexplained_flow_is_enough_to_fail(self):
        with mock.patch.dict(v.FIXTURES["network_flow_30d"],
                             {"unexpected_permitted_flows": 1}):
            r = by_id(v.evaluate())["KSI-CNA-RNT"]
        self.assertEqual(r["status"], "false")


class TestD_EvidenceIntegrity(unittest.TestCase):

    def test_generated_evidence_verifies(self):
        with tempfile.TemporaryDirectory() as d:
            write_evidence(d)
            self.assertEqual(run_verify(d), 0)

    def test_altered_evidence_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            write_evidence(d)
            path = os.path.join(d, "security-decision-record.json")
            with open(path, "rb") as f:
                data = f.read()
            # Same length, one value changed: flip the first failing KSI to true.
            tampered = data.replace(b'"status": "false"', b'"status": "true" ', 1)
            self.assertNotEqual(tampered, data)
            self.assertEqual(len(tampered), len(data))
            with open(path, "wb") as f:
                f.write(tampered)
            self.assertEqual(run_verify(d), 1)

    def test_missing_evidence_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            write_evidence(d)
            os.remove(os.path.join(d, "ongoing-certification-report.json"))
            self.assertEqual(run_verify(d), 1)

    def test_published_evidence_matches_a_fresh_run(self):
        with tempfile.TemporaryDirectory() as d:
            for name, blob in write_evidence(d):
                with open(os.path.join(EVIDENCE, name), "rb") as f:
                    self.assertEqual(f.read(), blob, name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
