#!/usr/bin/env python3
"""Automated verification suite for status.openOODA.org (index.html)."""
import os
import re
import sys

STATUS_HTML = "/Projects/openOODA/status/index.html"


def main() -> int:
    if not os.path.isfile(STATUS_HTML):
        print(f"FAIL: missing {STATUS_HTML}", file=sys.stderr)
        return 1

    with open(STATUS_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fail-closed Zero-Trust privacy gate
    forbidden = re.compile(
        r"100\.102\.|100\.88\.|100\.66\.|100\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
        r"|zebes|ringmaster|spotlight|starjammer|11435|/home/ubermetroid|~04:00|04:30|\$[0-9]|\$",
        re.IGNORECASE,
    )
    matches = forbidden.findall(html)
    assert not matches, f"Zero-Trust leak detected: {matches[:5]}"

    # 2. 90% Soft Throttle / 95% Hard Cutoff (>=5% Reserve Floor)
    assert "90% Soft Throttle" in html, "Missing 90% Soft Throttle policy text"
    assert "95% Hard Cutoff" in html, "Missing 95% Hard Cutoff policy text"
    assert 'class="quota-throttle-line" style="left:90%;"' in html, "Missing 90% soft throttle marker line"
    assert 'class="quota-target-line" style="left:95%;"' in html, "Missing 95% hard cutoff marker line"

    # 3. Interactive sorting controls (all 5 CRT sort buttons)
    expected_buttons = [
        ('data-sort="rem-pct"', "[ SORT: % LEFT (DEFAULT) ]"),
        ('data-sort="reset-sec"', "[ SORT: NEXT RESET ]"),
        ('data-sort="tps"', "[ SORT: LIVE TOK/SEC ]"),
        ('data-sort="capacity"', "[ SORT: CYCLE CAPACITY ]"),
        ('data-sort="name"', "[ SORT: AGENT NAME ]"),
    ]
    for attr, label in expected_buttons:
        assert attr in html, f"Missing sort button attribute {attr}"
        assert label in html, f"Missing sort button label {label}"

    # 4. Data attributes on every .quota-row card
    quota_rows = re.findall(r'<div class="quota-row"[^>]+>', html)
    assert len(quota_rows) == 5, f"Expected 5 .quota-row elements, found {len(quota_rows)}"
    required_attrs = [
        "data-name=",
        "data-rem-pct=",
        "data-used-pct=",
        "data-reset-sec=",
        "data-tps=",
        "data-capacity=",
    ]
    for row_tag in quota_rows:
        for attr in required_attrs:
            assert attr in row_tag, f"Missing {attr} on .quota-row: {row_tag}"

    # 5. JS sort handler and emerald phosphor (#50fa7b) highlight
    assert "window.sortQuotaGraph" in html, "Missing window.sortQuotaGraph handler"
    assert "#50fa7b" in html, "Missing emerald phosphor (#50fa7b) color definition"
    assert ".sort-btn.active" in html, "Missing .sort-btn.active style rule"

    # 6. 5-GPU live telemetry cards (GPU-00 .. GPU-04)
    for gpu_idx in range(5):
        assert f"GPU-0{gpu_idx}" in html, f"Missing GPU-0{gpu_idx} telemetry card"

    print("PASS: test_status.py (Zero-Trust, 90%/95% quota thresholds, 5 sort controls, 6 data-* attrs, 5 GPUs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
