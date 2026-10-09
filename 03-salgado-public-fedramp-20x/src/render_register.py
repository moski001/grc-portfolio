#!/usr/bin/env python3
"""
render_register.py — refresh the KSI Validation Register workbook from evidence

Rewrites the result columns of the "KSI Validation Register" sheet from
evidence/security-decision-record.json so the human-readable register cannot
drift from the machine-readable record. Formatting and the analyst-written
sheets (Drift Findings, Class Requirements, Method & Legend) are left alone.

Usage:
    python3 src/ksi_validator.py          # regenerate evidence first
    python3 src/render_register.py        # then refresh the register
"""

import json
import os
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
SDR = os.path.join(HERE, "..", "evidence", "security-decision-record.json")
XLSX = os.path.join(HERE, "..", "artifacts", "ksi_validation_register.xlsx")
SHEET = "KSI Validation Register"
FIRST_ROW = 5


def fmt(v):
    return str(v)


def main():
    with open(SDR) as f:
        sdr = json.load(f)
    wb = openpyxl.load_workbook(XLSX)
    ws = wb[SHEET]

    rows = {ws.cell(r, 1).value: r for r in range(FIRST_ROW, ws.max_row + 1) if ws.cell(r, 1).value}
    missing = []
    for k in sdr["key_security_indicators"]:
        r = rows.get(k["ksi_id"])
        if r is None:
            missing.append(k["ksi_id"])
            continue
        cp = next(v for v in k["validations"] if v["method_type"] == "control-plane")
        ob = next(v for v in k["validations"] if v["method_type"] != "control-plane")
        metrics = "; ".join(f"{m}={fmt(v)}" for val in (cp, ob) for m, v in val["metrics"].items())
        ws.cell(r, 2).value = k["ksi_family"]
        ws.cell(r, 3).value = k["ksi_name"]
        ws.cell(r, 4).value = k["ksi_statement"]
        ws.cell(r, 5).value = ", ".join(k["related_sp_800_53_controls"])
        ws.cell(r, 6).value = cp["method"]
        ws.cell(r, 7).value = cp["result"].upper()
        ws.cell(r, 8).value = ob["method"]
        ws.cell(r, 9).value = ob["result"].upper()
        ws.cell(r, 10).value = k["status"].upper()
        ws.cell(r, 11).value = "YES" if k["drift_detected"] else "No"
        ws.cell(r, 12).value = metrics

    if missing:
        sys.exit(f"KSIs in the evidence but not in the register: {', '.join(missing)}")

    wb.save(XLSX)
    print(f"Refreshed {len(sdr['key_security_indicators'])} KSI rows in {os.path.normpath(XLSX)}")


if __name__ == "__main__":
    main()
