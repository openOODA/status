#!/usr/bin/env python3
"""Automated layout, overflow, and telemetry verification suite for openOODA/status."""

import os
import re
import unittest
from html.parser import HTMLParser

STATUS_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML = os.path.join(STATUS_DIR, "index.html")
ECO_SYNC_BIN = "/home/ubermetroid/.local/bin/eco-sync-status"


class CardStructureParser(HTMLParser):
    """Validates HTML tag nesting and extracts card blocks and segmented bars."""

    def __init__(self):
        super().__init__()
        self.gpu_cards = 0
        self.stat_cards = 0
        self.quota_rows = 0
        self.ns_cards = 0
        self.gpu_seg_tracks = 0
        self.sort_buttons = []
        self.in_gpu_card = 0
        self.in_seg_bar = False
        self.gpu_seg_bars = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        cls = attr_dict.get("class", "")
        classes = set(cls.split())
        if "gpu-card" in classes:
            self.gpu_cards += 1
            self.in_gpu_card = 1
        elif self.in_gpu_card > 0 and tag == "div":
            self.in_gpu_card += 1

        if "stat-card" in classes:
            self.stat_cards += 1
        if "quota-row" in classes:
            self.quota_rows += 1
        if "ns-card" in classes:
            self.ns_cards += 1
        if "gpu-seg-track" in classes:
            self.gpu_seg_tracks += 1
        if "sort-btn" in classes and "data-sort" in attr_dict:
            self.sort_buttons.append(attr_dict["data-sort"])
        if self.in_gpu_card > 0 and "seg-bar" in classes:
            self.in_seg_bar = True

    def handle_endtag(self, tag):
        if self.in_seg_bar and tag in ("span", "code"):
            self.in_seg_bar = False
        if self.in_gpu_card > 0 and tag == "div":
            self.in_gpu_card -= 1

    def handle_data(self, data):
        if self.in_seg_bar:
            txt = data.strip()
            if txt:
                self.gpu_seg_bars.append(txt)


def extract_css_rule(css_text: str, selector: str) -> str:
    """Return the declarations inside a CSS selector block."""
    pattern = re.compile(re.escape(selector) + r"\s*\{([^}]*)\}", re.S)
    matches = pattern.findall(css_text)
    return "\n".join(matches)


class TestStatusPageOverflowAndTelemetry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            cls.html = f.read()
        with open(ECO_SYNC_BIN, "r", encoding="utf-8") as f:
            cls.sync_script = f.read()
        style_match = re.search(r"<style>(.*?)</style>", cls.html, re.S)
        cls.css = style_match.group(1) if style_match else ""

    def test_01_live_5_gpu_header_and_five_cards(self):
        """Verify Section [1] header and all 5 GPU cards (GPU-00..GPU-04) exist."""
        self.assertIn(
            "-- [1] LIVE 5-GPU HARDWARE TELEMETRY (GPU-00..GPU-04 // ANONYMIZED NODES) --",
            self.html,
        )
        for idx in range(5):
            self.assertIn(f"GPU-0{idx}", self.html)

        parser = CardStructureParser()
        parser.feed(self.html)
        self.assertEqual(parser.gpu_cards, 5, "Expected exactly 5 .gpu-card elements")
        self.assertEqual(
            parser.gpu_seg_tracks,
            10,
            "Expected 10 responsive CSS .gpu-seg-track bars (VRAM + UTIL across 5 GPUs)",
        )
        self.assertEqual(len(parser.gpu_seg_bars), 10)
        for bar in parser.gpu_seg_bars:
            self.assertLessEqual(
                len(bar),
                10,
                f"GPU segmented bar '{bar}' exceeds 10 blocks and risks overflowing narrow cards",
            )

    def test_02_gpu_grid_and_card_overflow_css(self):
        """Verify .gpu-grid and .gpu-card CSS prevent horizontal text/bar overflow at all viewports."""
        gpu_grid_css = extract_css_rule(self.css, ".gpu-grid")
        self.assertIn("grid-template-columns", gpu_grid_css)
        # Ensure minimum column width is >= 280px (e.g. 320px) so 5 cards wrap cleanly instead of squeezing to 210px
        col_widths = [int(x) for x in re.findall(r"(\d+)px", gpu_grid_css) if int(x) >= 200]
        self.assertTrue(
            any(w >= 280 for w in col_widths),
            f".gpu-grid minmax column width must be >= 280px, got: {gpu_grid_css}",
        )

        for selector in [".gpu-card", ".stat-card", ".quota-row", ".ns-card", ".panel", ".org-push-row"]:
            rule = extract_css_rule(self.css, selector)
            self.assertIn(
                "min-width: 0",
                rule,
                f"{selector} is missing 'min-width: 0' overflow protection",
            )
            self.assertIn(
                "overflow: hidden",
                rule,
                f"{selector} is missing 'overflow: hidden' boundary containment",
            )

        gpu_bar_line_css = extract_css_rule(self.css, ".gpu-bar-line")
        self.assertIn("flex-wrap: wrap", gpu_bar_line_css)
        self.assertIn("min-width: 0", gpu_bar_line_css)
        self.assertIn("overflow: hidden", gpu_bar_line_css)

        gpu_seg_track_css = extract_css_rule(self.css, ".gpu-seg-track")
        self.assertIn("max-width: 100%", gpu_seg_track_css)
        self.assertIn("overflow: hidden", gpu_seg_track_css)

        badge_css = extract_css_rule(self.css, ".term-badge")
        self.assertIn("max-width: 100%", badge_css)
        self.assertIn("overflow: hidden", badge_css)
        self.assertIn("text-overflow: ellipsis", badge_css)

    def test_03_simulated_card_content_fit_across_viewports(self):
        """Verify computed card content width never exceeds clientWidth across mobile (320px) and desktop (1180px)."""
        parser = CardStructureParser()
        parser.feed(self.html)
        # At 320px mobile viewport: card inner width is ~260px; at 1180px desktop with minmax(320px, 1fr):
        # 3 columns per row = ~366px per card (inner width ~342px).
        # With flex-wrap: wrap on .gpu-bar-line, each unbreakable token must fit inside 260px (~37 monospace chars).
        for bar in parser.gpu_seg_bars:
            px_width = len(bar) * 7.2  # 11px monospace char width ~6.6-7.2px
            self.assertLessEqual(
                px_width,
                100.0,
                f"Segmented bar '{bar}' ({px_width:.1f}px) is too wide for card flex line",
            )

    def test_04_interactive_sort_and_throttle_rules_preserved(self):
        """Verify window.sortQuotaGraph and 90% Soft Throttle / 95% Hard Cutoff rules are preserved."""
        self.assertIn("window.sortQuotaGraph", self.html)
        self.assertIn("window.sortQuotaGraph", self.sync_script)

        parser = CardStructureParser()
        parser.feed(self.html)
        self.assertEqual(
            parser.sort_buttons,
            ["rem-pct", "reset-sec", "tps", "capacity", "name"],
            "All 5 interactive sort buttons (% Left, Next Reset, Live tok/sec, Cycle Capacity, Agent Name) must be present",
        )
        self.assertEqual(parser.quota_rows, 5, "All 5 agent quota rows must be rendered")
        self.assertIn('left:90%;', self.html, "90% Soft Throttle line must be rendered")
        self.assertIn('left:95%;', self.html, "95% Hard Cutoff line must be rendered")
        self.assertIn("90% Soft Throttle", self.html)
        self.assertIn("95% Hard Cutoff", self.html)

    def test_05_zero_trust_privacy_gate(self):
        """Verify zero internal IPs, hostnames, ports, paths, or dollar amounts leak into index.html."""
        forbidden = re.compile(
            r"100\.\d{1,3}\.\d{1,3}\.\d{1,3}|zebes|ringmaster|spotlight|starjammer|11435|/home/ubermetroid|~04:00|04:30|\$[0-9]|\$",
            re.I,
        )
        matches = forbidden.findall(self.html)
        self.assertEqual(matches, [], f"Zero-Trust privacy gate violation: {matches}")

    def test_06_devin_swe2_max_and_swe2_flash_free_promo_telemetry(self):
        """Verify Devin displays Nov 4 SWE-2 Max + SWE-2 Flash Max (3x speed) Free Unlimited Promo thru Nov 30 with live burn."""
        self.assertIn(
            "[ FREE UNLIMITED PROMO THRU NOV 30 // SWE-2 MAX + SWE-2 FLASH MAX (3X SPEED) ]",
            self.html,
        )
        self.assertIn("SWE-2 Max + SWE-2 Flash Max", self.html)
        self.assertIn("FREE PROMO Nov30 (23.0M+ burn)", self.html)
        burn_m = re.search(r"24h burn:\s*([0-9.]+)M\+", self.html)
        self.assertIsNotNone(burn_m, "Devin live 24h burn must be displayed")
        self.assertGreaterEqual(float(burn_m.group(1)), 23.0, "Expected Devin 24h burn >= 23.0M+")
        self.assertNotIn("SHADOW QUOTA:", self.html)
        self.assertNotIn("API REPORTS 0% (LAG/PROMO)", self.html)
        m = re.search(r'<div class="quota-row" data-name="devin" data-rem-pct="(\d+)" data-used-pct="(\d+)"', self.html)
        self.assertIsNotNone(m, "Devin quota-row must exist with data-rem-pct and data-used-pct")
        rem_pct = int(m.group(1))
        used_pct = int(m.group(2))
        self.assertEqual(rem_pct, 100, f"Expected Devin promo rem_pct == 100%, got {rem_pct}%")
        self.assertEqual(used_pct, 0, f"Expected Devin promo used_pct == 0%, got {used_pct}%")
        self.assertIn("<code>wQ:p1</code>", self.html, "wQ:p1 must be present in the Herdr pane matrix")
        self.assertIn("<code>wQ:p2</code>", self.html, "wQ:p2 must be present in the Herdr pane matrix")
        self.assertIn("idlescreen (ooda)", self.html, "idlescreen (ooda) workspace must be present in the Herdr pane matrix")
        self.assertIn("18 Layer/Project Panes", self.html, "18 Layer/Project Panes summary must be present")


if __name__ == "__main__":
    unittest.main()

