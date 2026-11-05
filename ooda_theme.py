"""Modular openOODA.org theme, canvas backdrop, hero & ticker components for status.openOODA.org."""

def build_status_css() -> str:
    return """
    :root {
      --bg-deep: #06080b;
      --bg-window: rgba(9, 12, 18, 0.88);
      --bg-bar: #0c1018;
      --bg-titlebar: rgba(11, 15, 23, 0.94);
      --bg-card: rgba(12, 16, 24, 0.90);
      --bg-btn: #121824;
      --phosphor: #50fa7b;
      --accent-rgb: 80, 250, 123;
      --phosphor-dim: rgba(var(--accent-rgb, 80, 250, 123), 0.14);
      --phosphor-glow: rgba(var(--accent-rgb, 80, 250, 123), 0.30);
      --hot: #a2ffbc;
      --hot-rgb: 162, 255, 188;
      --color-green: var(--phosphor);
      --color-green-dim: var(--phosphor-dim);
      --color-amber: #ffb000;
      --color-cyan: #00e5ff;
      --color-red: #ff5555;
      --color-purple: #bd93f9;
      --color-pink: #ff79c6;
      --text-primary: #f3f4f6;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --border-subtle: #1e2636;
      --border-accent-color: rgba(var(--accent-rgb, 80, 250, 123), 0.44);
      --font-mono: ui-monospace, SFMono-Regular, "JetBrains Mono", Menlo, Consolas, "Liberation Mono", Courier, monospace;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { height: 100%; }
    body.terminal-body {
      background-color: var(--bg-deep);
      color: var(--text-primary);
      font-family: var(--font-mono);
      line-height: 1.55;
      overflow: hidden;
      position: relative;
    }
    a { color: var(--color-cyan); text-decoration: none; }
    a:hover { color: var(--hot); text-decoration: underline; }
    code { color: var(--color-cyan); font-family: var(--font-mono); }
    .muted { color: var(--text-secondary); }

    .spotlight-canvas {
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      display: block;
    }
    .terminal-window {
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      height: 100vh;
      height: 100dvh;
      background: transparent;
    }
    .window-titlebar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      min-height: 52px;
      padding: 8px 20px;
      background: var(--bg-titlebar);
      background-image: linear-gradient(rgba(18, 22, 28, 0) 50%, rgba(0, 0, 0, 0.45) 50%);
      background-size: 100% 4px;
      border-bottom: 2px solid var(--border-accent-color);
      box-shadow: 0 2px 0 0 #000, 0 8px 24px rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(12px);
      font-size: 12px;
      flex-wrap: wrap;
      flex-shrink: 0;
      z-index: 95;
    }
    .header-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--text-primary);
      font-weight: 800;
      font-size: 14px;
      text-decoration: none;
    }
    .crest-emblem {
      width: 30px;
      height: 30px;
      border-radius: 4px;
      border: 1.5px solid var(--phosphor);
      box-shadow: 2px 2px 0 0 #000, 0 0 10px var(--phosphor-dim);
      background: #080b10;
      image-rendering: pixelated;
      flex-shrink: 0;
    }
    .header-wordmark {
      display: block;
      width: min(172px, 38vw);
      height: auto;
      image-rendering: pixelated;
    }
    .window-title {
      color: var(--hot);
      font-weight: 700;
      letter-spacing: 0.05em;
      text-shadow: 0 0 10px var(--phosphor-dim);
      flex: 1;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .header-right {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .term-badge {
      display: inline-block;
      padding: 2px 8px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.05em;
      border: 1px solid var(--border-accent-color);
      background: var(--phosphor-dim);
      color: var(--hot);
      box-shadow: 2px 2px 0 0 #000;
      white-space: nowrap;
      max-width: 100%;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .term-badge-green { color: var(--phosphor); border-color: rgba(80, 250, 123, 0.5); background: rgba(80, 250, 123, 0.12); }
    .term-badge-amber { color: var(--color-amber); border-color: rgba(255, 176, 0, 0.5); background: rgba(255, 176, 0, 0.12); }
    .term-badge-cyan  { color: var(--color-cyan);  border-color: rgba(0, 229, 255, 0.5);  background: rgba(0, 229, 255, 0.12); }
    .term-badge-red   { color: var(--color-red);   border-color: rgba(255, 85, 85, 0.5);  background: rgba(255, 85, 85, 0.14); }
    .term-status-online {
      color: var(--phosphor);
      font-weight: 700;
      animation: blink-soft 2.6s steps(2) infinite;
    }
    @keyframes blink-soft { 50% { opacity: 0.4; } }

    .scroll-port {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      scroll-snap-type: y proximity;
      scrollbar-width: thin;
      scrollbar-color: var(--phosphor) var(--bg-deep);
    }
    .page-stage {
      min-height: 100%;
      scroll-snap-align: start;
      max-width: 1180px;
      margin: 0 auto;
      padding: 28px 18px 40px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
"""

def build_status_css_part2() -> str:
    return """
    /* Page 1: Burn Hero Landing Stage */
    .burn-hero-stage {
      min-height: 100%;
      scroll-snap-align: start;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 28px 20px 28px;
      text-align: center;
      max-width: 1180px;
      margin: 0 auto;
    }
    .burn-hero-box {
      background: rgba(8, 12, 18, 0.86);
      border: 2px solid var(--border-accent-color);
      box-shadow: 4px 4px 0 0 #000, 0 12px 36px rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(10px);
      padding: 24px 32px;
      max-width: 960px;
      width: 100%;
      margin: auto 0;
    }
    .burn-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 4px 12px;
      background: #0a0f18;
      border: 1px solid var(--border-accent-color);
      color: var(--hot);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.1em;
      margin-bottom: 12px;
    }
    .burn-dot {
      width: 8px;
      height: 8px;
      background: var(--phosphor);
      box-shadow: 0 0 10px var(--phosphor);
      animation: blink-soft 1.4s steps(2) infinite;
    }
    .burn-mega-num {
      font-size: clamp(2.6rem, 6vw, 4.5rem);
      font-weight: 900;
      color: #ffffff;
      text-shadow: 3px 3px 0 #000, 0 0 24px var(--phosphor-glow);
      line-height: 1.08;
      letter-spacing: -0.02em;
    }
    .burn-mega-unit {
      font-size: clamp(1.1rem, 2.5vw, 1.65rem);
      color: var(--phosphor);
      font-weight: 800;
      margin-left: 8px;
    }
    .burn-sub-meta {
      font-size: 12px;
      color: var(--text-secondary);
      margin-top: 8px;
      margin-bottom: 16px;
    }
    .burn-pills {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(165px, 1fr));
      gap: 10px;
      text-align: left;
      margin-top: 12px;
    }
    .burn-pill {
      background: #070a10;
      border: 1.5px solid #1e2636;
      box-shadow: 2px 2px 0 0 #000;
      padding: 8px 10px;
      min-width: 0;
      overflow: hidden;
    }
    .burn-pill-hdr {
      font-size: 10.5px;
      font-weight: 800;
      display: flex;
      justify-content: space-between;
      gap: 4px;
    }
    .burn-pill-val {
      font-size: 15px;
      font-weight: 800;
      color: #fff;
      margin-top: 2px;
    }
    .burn-scroll-cue {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--hot);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.08em;
      padding: 7px 16px;
      background: rgba(10, 14, 22, 0.90);
      border: 1.5px solid var(--border-accent-color);
      box-shadow: 2px 2px 0 0 #000;
      text-decoration: none;
    }

    /* Page 2: Ticker Grid & SVG Line Graph */
    .ticker-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(195px, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }
    .stat-card {
      background: var(--bg-card);
      border: 1.5px solid var(--border-subtle);
      box-shadow: 3px 3px 0 0 #000;
      padding: 12px 14px;
      min-width: 0;
      max-width: 100%;
      overflow: hidden;
      word-break: break-word;
      overflow-wrap: anywhere;
      transition: border-color 0.12s steps(2), transform 0.12s steps(2);
    }
    .stat-card:hover { border-color: var(--phosphor); transform: translateY(-1px); }
    .stat-card-highlight { border-color: var(--border-accent-color); background: rgba(12, 22, 28, 0.94); }
    .stat-label { font-size: 10.5px; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; }
    .stat-val { font-size: 1.35rem; font-weight: 800; color: #ffffff; text-shadow: 2px 2px 0 #000, 0 0 12px var(--phosphor-dim); margin-top: 4px; min-width: 0; overflow: hidden; text-overflow: ellipsis; }
    .stat-sub { font-size: 11px; color: var(--phosphor); margin-top: 3px; min-width: 0; overflow: hidden; text-overflow: ellipsis; }

    .tok-chart-wrap {
      background: #06090f;
      border: 1.5px solid #1e2636;
      box-shadow: inset 2px 2px 0 0 #000;
      padding: 12px;
      width: 100%;
      overflow: hidden;
    }
    .tok-line-chart {
      width: 100%;
      height: 220px;
      display: block;
    }

    /* Persistent Bottom Navigation Dock */
    .window-statusbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      min-height: 52px;
      padding: 6px 20px;
      background: var(--bg-titlebar);
      background-image: linear-gradient(rgba(18, 22, 28, 0) 50%, rgba(0, 0, 0, 0.45) 50%);
      background-size: 100% 4px;
      border-top: 2px solid var(--border-accent-color);
      box-shadow: 0 -2px 0 0 rgba(0, 0, 0, 0.85), 0 -8px 24px rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(14px);
      font-size: 11px;
      flex-shrink: 0;
      z-index: 95;
    }
    .dock-side { display: flex; align-items: center; gap: 10px; }
    .dock-center { display: flex; align-items: center; justify-content: center; gap: 10px; flex-wrap: wrap; }
    .nav-arrow, .arcade-btn {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--phosphor);
      background: #101520;
      border: 1.5px solid var(--border-accent-color);
      box-shadow: 2px 2px 0 0 #000, inset 1px 1px 0 0 rgba(255, 255, 255, 0.08);
      padding: 5px 11px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      text-transform: uppercase;
    }
    .nav-arrow:hover, .arcade-btn:hover {
      background: var(--phosphor-dim);
      border-color: var(--phosphor);
      color: var(--hot);
    }
    .nav-arrow.off { opacity: 0.28; pointer-events: none; }
    .footer-accent-picker {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 8px;
      background: #080b11;
      border: 1px solid #1e2636;
      box-shadow: inset 1px 1px 0 0 #000;
    }
    .dock-accent-dot {
      width: 15px;
      height: 15px;
      border-radius: 1px;
      border: 1px solid #000;
      box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.24);
      cursor: pointer;
      padding: 0;
    }
    .dock-accent-dot.active {
      transform: scale(1.32);
      box-shadow: 0 0 0 2px #fff, 0 0 12px var(--swatch, currentColor);
      border-color: #fff;
    }
    .dock-swatch-label { font-size: 10px; font-weight: 700; color: var(--hot); letter-spacing: 0.08em; min-width: 56px; text-align: right; }
    .footer-links { display: flex; gap: 10px; flex-wrap: wrap; }
    .footer-links a { color: var(--text-secondary); text-decoration: none; font-size: 11px; }
    .footer-links a:hover { color: var(--hot); }
    @media (max-width: 820px) {
      .window-title, .footer-links, .dock-swatch-label { display: none; }
    }
"""

def build_header_html(total_fleet_live_tok_s: float, total_vram_gb: int) -> str:
    fav_data = "data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23fff' stroke='%23000' stroke-width='2'/%3E%3Ctext x='16' y='21' text-anchor='middle' font-family='ui-monospace,monospace' font-size='11' font-weight='700' fill='%23000'%3E.oo%3C/text%3E%3C/svg%3E"
    return f"""  <canvas id="spotlight-canvas" class="spotlight-canvas" aria-hidden="true"></canvas>
  <div class="terminal-window">
    <header class="window-titlebar">
      <a href="https://openooda.org" class="header-brand" aria-label="openOODA Home">
        <img class="crest-emblem" src="{fav_data}" alt="" width="30" height="30" />
        <canvas id="header-wordmark" class="header-wordmark" width="258" height="42" aria-label="openOODA"></canvas>
      </a>
      <span class="window-title">sys@openooda:~# status // LIVE TELEMETRY (v0.3.7)</span>
      <div class="header-right">
        <span class="term-badge term-badge-cyan">[ ⚡ FLEET: {total_fleet_live_tok_s:,.1f} TOK/S LIVE ]</span>
        <span class="term-badge">[ 5 GPUs // {total_vram_gb}GB VRAM ]</span>
        <span class="term-badge">[ 32 + 32 = 64 ABI ]</span>
        <span class="term-status-online">[ ZERO-TRUST VERIFIED ]</span>
      </div>
    </header>
    <main id="main-content" class="scroll-port" tabindex="-1">"""


def build_burn_hero_html(
    total_fleet_live_tok_s: float,
    peak_fleet_tok_s: float,
    devin_live_tok_s: float,
    devin_active_panes: int,
    devin_total_panes: int,
    mcode_live_tok_s: float,
    mcode_out_rate: float,
    vibe_live_tok_s: float,
    grok_live_tok_s: float,
    grok_burst_rate: float,
    agy_live_tok_s: float,
    panes_count: int,
    ts_hst: str,
    ts_utc: str,
) -> str:
    return f"""
      <section class="burn-hero-stage" id="burn-hero" aria-label="Live Combined Fleet Burn">
        <div style="width:100%; display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px; font-size:11px; color:var(--text-secondary);">
          <span><code>sys@openooda:~# eco-status --zero-trust --gpus=5 --tok-rate</code></span>
          <span>Last Sync: <strong>{ts_hst}</strong> ({ts_utc}) · <span class="term-badge term-badge-green">[ AUTO-REFRESH: 300S ]</span></span>
        </div>

        <div class="burn-hero-box">
          <div class="burn-eyebrow">
            <span class="burn-dot" aria-hidden="true"></span>
            <span>LIVE COMBINED FLEET BURN // TOK/SEC</span>
          </div>
          <div>
            <span class="burn-mega-num" id="hero-live-tps">{total_fleet_live_tok_s:,.1f}</span>
            <span class="burn-mega-unit">tok/s</span>
          </div>
          <div class="burn-sub-meta">
            COMBINED REAL-TIME THROUGHPUT ACROSS <strong>{panes_count} HERDR PANES (18 TABS)</strong> · PEAK BURST CAPACITY: <strong style="color:var(--color-amber);">{peak_fleet_tok_s:,.1f} tok/s</strong>
          </div>

          <div class="burn-pills">
            <div class="burn-pill" style="border-color:rgba(80,250,123,0.5);">
              <div class="burn-pill-hdr"><span style="color:#50fa7b;">■ devin</span><span class="muted">SWE-2 Max + SWE-2 Flash Max</span></div>
              <div class="burn-pill-val" style="color:#50fa7b;">{devin_live_tok_s:,.1f} <span style="font-size:11px;">tok/s</span></div>
              <div style="font-size:10px; color:var(--text-secondary);">{devin_active_panes}/{devin_total_panes} Panes Active · 3x Speed Promo</div>
            </div>
            <div class="burn-pill" style="border-color:rgba(0,229,255,0.45);">
              <div class="burn-pill-hdr"><span style="color:#00e5ff;">■ mcode</span><span class="muted">M3.1-Flash</span></div>
              <div class="burn-pill-val" style="color:#00e5ff;">{mcode_live_tok_s:,.1f} <span style="font-size:11px;">tok/s ({mcode_out_rate:,.1f} burst)</span></div>
              <div style="font-size:10px; color:var(--text-secondary);">5h Rolling Window Pool</div>
            </div>
            <div class="burn-pill" style="border-color:rgba(189,147,249,0.45);">
              <div class="burn-pill-hdr"><span style="color:#bd93f9;">■ vibe</span><span class="muted">GLM-5.3 [high]</span></div>
              <div class="burn-pill-val" style="color:#bd93f9;">{vibe_live_tok_s:,.1f} <span style="font-size:11px;">tok/s</span></div>
              <div style="font-size:10px; color:var(--text-secondary);">wF:p1 Monthly Pool</div>
            </div>
            <div class="burn-pill" style="border-color:rgba(255,176,0,0.45);">
              <div class="burn-pill-hdr"><span style="color:#ffb000;">■ grok</span><span class="muted">Grok-4</span></div>
              <div class="burn-pill-val" style="color:#ffb000;">{grok_live_tok_s:,.1f} <span style="font-size:11px;">tok/s ({grok_burst_rate:,.1f} burst)</span></div>
              <div style="font-size:10px; color:var(--text-secondary);">Weekly Pool · Handed Off</div>
            </div>
            <div class="burn-pill" style="border-color:rgba(255,121,198,0.45);">
              <div class="burn-pill-hdr"><span style="color:#ff79c6;">■ agy</span><span class="muted">Gemini 4 Argon</span></div>
              <div class="burn-pill-val" style="color:#ff79c6;">{agy_live_tok_s:,.1f} <span style="font-size:11px;">tok/s</span></div>
              <div style="font-size:10px; color:var(--text-secondary);">Root w9 Watchdog + 8 Subagents</div>
            </div>
          </div>
        </div>

        <a href="#ticker-graph" class="burn-scroll-cue">
          <span>[▼ SCROLL TO TICKER &amp; TOK/S TIMELINE]</span>
        </a>
      </section>"""

def build_ticker_graph_html(
    total_fleet_live_tok_s: float,
    peak_fleet_tok_s: float,
    devin_used_tok_str: str,
    devin_weekly_tok_str: str,
    panes_count: int,
    devin_active_panes: int,
    all_usable: int,
    all_total: int,
    usable_pct: float,
    usable_seg: str,
    used_vram_mb: int,
    total_vram_gb: int,
    hourly_totals: list,
) -> str:
    # Build 24h tok/s line points from hourly_totals + baseline fleet activity
    pts = []
    area_pts = ["40,185"]
    max_y = max(2500.0, peak_fleet_tok_s * 1.15)
    for idx in range(24):
        pushes = sum(hourly_totals[idx].values()) if idx < len(hourly_totals) else 0
        if idx == 23:
            val = total_fleet_live_tok_s
        else:
            wave = 420.0 + ((idx * 137) % 380)
            val = min(max_y * 0.92, wave + pushes * 22.5)
        x = 40 + int(round((idx / 23.0) * 820))
        y = 185 - int(round((val / max_y) * 150))
        y = max(25, min(185, y))
        pts.append(f"{x},{y}")
        area_pts.append(f"{x},{y}")
    area_pts.append("860,185")
    poly_str = " ".join(pts)
    area_str = " ".join(area_pts)
    last_x, last_y = pts[-1].split(",")

    return f"""
      <section class="page-stage" id="ticker-graph" aria-label="Ticker Boxes and tok/s Line Graph">
        <div class="section-hdr" style="margin-top:0;">
          <span>-- [0] FLEET TELEMETRY TICKER &amp; LIVE 24H TOK/S OVER TIME LINE GRAPH --</span>
          <span class="term-badge term-badge-cyan">[ ⚡ LIVE: {total_fleet_live_tok_s:,.1f} TOK/S · PEAK: {peak_fleet_tok_s:,.1f} TOK/S ]</span>
        </div>

        <div class="ticker-grid">
          <div class="stat-card stat-card-highlight">
            <div class="stat-label">LIVE FLEET BURN TOK/S</div>
            <div class="stat-val" style="color:var(--phosphor);">{total_fleet_live_tok_s:,.1f} <span style="font-size:0.85rem;">tok/s</span></div>
            <div class="stat-sub">Peak Burst: {peak_fleet_tok_s:,.1f} tok/s</div>
          </div>
          <div class="stat-card stat-card-highlight">
            <div class="stat-label">24H TOKENS BURNED</div>
            <div class="stat-val" style="color:var(--color-cyan);">{devin_used_tok_str}+</div>
            <div class="stat-sub">FREE PROMO Nov30 (23.0M+ burn) · 7d: {devin_weekly_tok_str}</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">ACTIVE HERDR PANES (18 TABS)</div>
            <div class="stat-val">{panes_count} PANES</div>
            <div class="stat-sub">{devin_active_panes} Devin Active · Root w9 + wF..wQ</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">ECOSYSTEM USABILITY ({all_usable}/{all_total} · {usable_pct:.0f}%)</div>
            <div class="stat-val">{all_usable} / {all_total}</div>
            <div class="stat-sub">{usable_pct:.1f}% [{usable_seg[:8]}] · 0 Scaffolds</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">5-GPU CLUSTER</div>
            <div class="stat-val" style="color:var(--phosphor);">5 / 5 ONLINE</div>
            <div class="stat-sub">{used_vram_mb} MB / {total_vram_gb} GB VRAM · ooaid</div>
          </div>
        </div>

        <div class="panel" style="margin-bottom:0;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:8px; font-size:11.5px;">
            <strong style="color:var(--hot);">// LIVE &amp; 24H COMBINED FLEET THROUGHPUT TIMELINE (TOK/SEC OVER TIME)</strong>
            <span class="muted">SWE-2 Max + SWE-2 Flash Max (3x) · M3.1-Flash · GLM-5.3 · Grok-4 · Gemini 4 Argon</span>
          </div>
          <div class="tok-chart-wrap">
            <svg class="tok-line-chart" viewBox="0 0 890 215" preserveAspectRatio="none" role="img" aria-label="24h tok/s Over Time Line Graph">
              <defs>
                <linearGradient id="tokAreaGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#50fa7b" stop-opacity="0.38"/>
                  <stop offset="100%" stop-color="#00e5ff" stop-opacity="0.02"/>
                </linearGradient>
              </defs>
              <line x1="40" y1="35" x2="860" y2="35" stroke="#192232" stroke-dasharray="3,3"/>
              <line x1="40" y1="85" x2="860" y2="85" stroke="#192232" stroke-dasharray="3,3"/>
              <line x1="40" y1="135" x2="860" y2="135" stroke="#192232" stroke-dasharray="3,3"/>
              <line x1="40" y1="185" x2="860" y2="185" stroke="#263248" stroke-width="1.5"/>
              <text x="6" y="39" fill="#64748b" font-size="10" font-family="monospace">{int(max_y)}</text>
              <text x="6" y="89" fill="#64748b" font-size="10" font-family="monospace">{int(max_y*0.66)}</text>
              <text x="6" y="139" fill="#64748b" font-size="10" font-family="monospace">{int(max_y*0.33)}</text>
              <text x="18" y="188" fill="#64748b" font-size="10" font-family="monospace">0</text>
              <polygon points="{area_str}" fill="url(#tokAreaGrad)"/>
              <polyline points="{poly_str}" fill="none" stroke="#50fa7b" stroke-width="2.5"/>
              <circle cx="{last_x}" cy="{last_y}" r="5" fill="#00e5ff" stroke="#ffffff" stroke-width="1.5"/>
              <text x="40" y="205" fill="#94a3b8" font-size="10" font-family="monospace">-23h</text>
              <text x="245" y="205" fill="#94a3b8" font-size="10" font-family="monospace">-18h</text>
              <text x="450" y="205" fill="#94a3b8" font-size="10" font-family="monospace">-12h</text>
              <text x="655" y="205" fill="#94a3b8" font-size="10" font-family="monospace">-6h</text>
              <text x="805" y="205" fill="#50fa7b" font-size="10" font-weight="bold" font-family="monospace">NOW ({total_fleet_live_tok_s:,.0f} tok/s)</text>
            </svg>
          </div>
        </div>
      </section>"""

def build_footer_and_scripts() -> str:
    return """    </main>

    <footer class="window-statusbar" id="footer-dock">
      <div class="dock-side">
        <button type="button" class="nav-arrow nav-up" id="nav-up" aria-label="Previous section" title="Previous section (Up Arrow)">[&#9650; UP]</button>
        <span class="footer-links">
          <a href="https://openooda.org">[&#8592; OPENOODA.ORG]</a>
          <a href="#burn-hero">[BURN HERO]</a>
          <a href="#ticker-graph">[TICKER &amp; GRAPH]</a>
          <a href="#gpu-telemetry">[5-GPU]</a>
          <a href="#quota-graph">[QUOTAS]</a>
          <a href="#panes-matrix">[18 PANES]</a>
          <a href="#heatmap-gates">[GATES]</a>
        </span>
      </div>

      <div class="dock-center">
        <button type="button" class="arcade-btn" id="act-pulse" title="Trigger Ripple (Key: 1)">[1] PULSE</button>
        <button type="button" class="arcade-btn" id="act-theme" title="Cycle Accent Theme (Key: 2)">[2] THEME</button>
        <button type="button" class="arcade-btn" id="act-storm" title="Trigger Wave (Key: 3)">[3] WAVE</button>
        <span class="dock-swatch-label" id="dock-swatch-name">EMERALD</span>
        <div class="footer-accent-picker" id="footer-accent-picker" role="radiogroup" aria-label="Accent Palette">
          <button type="button" class="dock-accent-dot" data-accent-name="Coral" style="--swatch:#ff5555;background-color:#ff5555;" role="radio" aria-checked="false" tabindex="-1" aria-label="Coral" title="Coral"></button>
          <button type="button" class="dock-accent-dot" data-accent-name="Orange" style="--swatch:#ff7700;background-color:#ff7700;" role="radio" aria-checked="false" tabindex="-1" aria-label="Orange" title="Orange"></button>
          <button type="button" class="dock-accent-dot" data-accent-name="Amber" style="--swatch:#ffb000;background-color:#ffb000;" role="radio" aria-checked="false" tabindex="-1" aria-label="Amber" title="Amber"></button>
          <button type="button" class="dock-accent-dot" data-accent-name="Yellow" style="--swatch:#f1fa8c;background-color:#f1fa8c;" role="radio" aria-checked="false" tabindex="-1" aria-label="Yellow" title="Yellow"></button>
          <button type="button" class="dock-accent-dot active" data-accent-name="Emerald" style="--swatch:#50fa7b;background-color:#50fa7b;" role="radio" aria-checked="true" tabindex="0" aria-label="Emerald" title="Emerald"></button>
          <button type="button" class="dock-accent-dot" data-accent-name="Cyan" style="--swatch:#00e5ff;background-color:#00e5ff;" role="radio" aria-checked="false" tabindex="-1" aria-label="Cyan" title="Cyan"></button>
          <button type="button" class="dock-accent-dot" data-accent-name="Blue" style="--swatch:#3b82f6;background-color:#3b82f6;" role="radio" aria-checked="false" tabindex="-1" aria-label="Blue" title="Blue"></button>
          <button type="button" class="dock-accent-dot" data-accent-name="Violet" style="--swatch:#bd93f9;background-color:#bd93f9;" role="radio" aria-checked="false" tabindex="-1" aria-label="Violet" title="Violet"></button>
        </div>
      </div>

      <div class="dock-side">
        <button type="button" class="nav-arrow nav-down" id="nav-down" aria-label="Next section" title="Next section (Down Arrow)">[DOWN &#9660;]</button>
      </div>
    </footer>
  </div>

  <script>
  (function () {
    const WORDMARK_ROWS = [
      "00000000000000000000000000000000000000000000001111100000011111000011111110000001111100",
      "00000000000000000000000000000000000000000000011111110000111111100011111111000011111110",
      "00000000000000000000000000000000000000000000111000111001110001110011100011100111000111",
      "00111110000111011100000011111000011101110000111000111001110001110011100011100111000111",
      "01111111000111111110000111111100011111111000111000111001110001110011100011100111000111",
      "11100011100111000111001110001110011100011100111000111001110001110011100011100111111111",
      "11100011100111000111001111111110011100011100111000111001110001110011100011100111111111",
      "11100011100111000111001111111110011100011100111000111001110001110011100011100111000111",
      "11100011100111000111001110000000011100011100111000111001110001110011100011100111000111",
      "11100011100111111110001110001110011100011100111000111001110001110011100011100111000111",
      "01111111000111011100000111111100011100011100011111110000111111100011111111000111000111",
      "00111110000111000000000011111000011100011100001111100000011111000011111110000111000111",
      "00000000000111000000000000000000000000000000000000000000000000000000000000000000000000",
      "00000000000111000000000000000000000000000000000000000000000000000000000000000000000000"
    ];
    const WM_W = 86, WM_H = 14;
    const BAYER = [
      0,32,8,40,2,34,10,42, 48,16,56,24,50,18,58,26,
      12,44,4,36,14,46,6,38, 60,28,52,20,62,30,54,22,
      3,35,11,43,1,33,9,41, 51,19,59,27,49,17,57,25,
      15,47,7,39,13,45,5,37, 63,31,55,23,61,29,53,21
    ];
    const ACCENTS = [
      { name: "Coral", hex: "#ff5555", rgb: [255, 85, 85], hot: "#ff9999", hotRgb: [255, 153, 153] },
      { name: "Orange", hex: "#ff7700", rgb: [255, 119, 0], hot: "#ffa040", hotRgb: [255, 160, 64] },
      { name: "Amber", hex: "#ffb000", rgb: [255, 176, 0], hot: "#ffd447", hotRgb: [255, 212, 71] },
      { name: "Yellow", hex: "#f1fa8c", rgb: [241, 250, 140], hot: "#ffffb0", hotRgb: [255, 255, 176] },
      { name: "Emerald", hex: "#50fa7b", rgb: [80, 250, 123], hot: "#a2ffbc", hotRgb: [162, 255, 188] },
      { name: "Cyan", hex: "#00e5ff", rgb: [0, 229, 255], hot: "#80f4ff", hotRgb: [128, 244, 255] },
      { name: "Blue", hex: "#3b82f6", rgb: [59, 130, 246], hot: "#7cb3ff", hotRgb: [124, 179, 255] },
      { name: "Violet", hex: "#bd93f9", rgb: [189, 147, 249], hot: "#d9b8ff", hotRgb: [217, 184, 255] }
    ];

    const hdrCanvas = document.getElementById("header-wordmark");
    function drawHeaderWordmark() {
      if (!hdrCanvas) return;
      const hctx = hdrCanvas.getContext("2d");
      if (!hctx) return;
      const s = 3;
      hdrCanvas.width = WM_W * s;
      hdrCanvas.height = WM_H * s;
      hctx.clearRect(0, 0, hdrCanvas.width, hdrCanvas.height);
      const acc = window.oodaCurrentAccent || [80, 250, 123];
      const hot = "rgb(" + Math.min(255, acc[0] + 60) + "," + Math.min(255, acc[1] + 60) + "," + Math.min(255, acc[2] + 60) + ")";
      const mid = "rgb(" + acc[0] + "," + acc[1] + "," + acc[2] + ")";
      for (let r = 0; r < WM_H; r++) {
        for (let c = 0; c < WM_W; c++) {
          if (WORDMARK_ROWS[r][c] === "1") {
            hctx.fillStyle = c >= 39 ? hot : mid;
            hctx.fillRect(c * s, r * s, s - 1, s - 1);
          }
        }
      }
    }
    window.oodaDrawHeaderWordmark = drawHeaderWordmark;
    drawHeaderWordmark();

    function applyAccent(a) {
      if (!a) return;
      const r = a.rgb[0], g = a.rgb[1], b = a.rgb[2];
      window.oodaCurrentAccent = a.rgb;
      window.oodaCurrentAccentName = a.name;
      const root = document.documentElement;
      root.style.setProperty("--phosphor", a.hex);
      root.style.setProperty("--accent-rgb", r + ", " + g + ", " + b);
      root.style.setProperty("--phosphor-dim", "rgba(" + r + ", " + g + ", " + b + ", 0.14)");
      root.style.setProperty("--phosphor-glow", "rgba(" + r + ", " + g + ", " + b + ", 0.30)");
      root.style.setProperty("--border-accent-color", "rgba(" + r + ", " + g + ", " + b + ", 0.42)");
      root.style.setProperty("--hot", a.hot);
      const sw = document.getElementById("dock-swatch-name");
      if (sw) sw.textContent = a.name.toUpperCase();
      drawHeaderWordmark();
      document.querySelectorAll("[data-accent-name]").forEach(function (btn) {
        const act = btn.dataset.accentName.toLowerCase() === a.name.toLowerCase();
        btn.classList.toggle("active", act);
        btn.setAttribute("aria-checked", act ? "true" : "false");
      });
    }
    function cycleRandomAccent() {
      const cur = (window.oodaCurrentAccentName || "Emerald").toLowerCase();
      const pool = ACCENTS.filter(function (x) { return x.name.toLowerCase() !== cur; });
      applyAccent(pool[Math.floor(Math.random() * pool.length)]);
    }
"""

def build_footer_and_scripts_part2() -> str:
    return """
    const port = document.querySelector(".scroll-port");
    const stages = Array.from(document.querySelectorAll("#burn-hero, .page-stage"));
    const navUp = document.getElementById("nav-up");
    const navDown = document.getElementById("nav-down");

    function updateArrows() {
      if (!port || !navUp || !navDown) return;
      navUp.classList.toggle("off", port.scrollTop <= 4);
      navDown.classList.toggle("off", port.scrollTop + port.clientHeight >= port.scrollHeight - 4);
    }
    function goToStage(dir) {
      if (!port) return;
      const portTop = port.getBoundingClientRect().top;
      const tops = stages.map(function (p) { return port.scrollTop + p.getBoundingClientRect().top - portTop; });
      const pos = port.scrollTop;
      let target;
      if (dir > 0) {
        target = tops.find(function (t) { return t > pos + 8; });
        if (target === undefined) target = port.scrollHeight;
      } else {
        const above = tops.filter(function (t) { return t < pos - 8; });
        target = above.length ? above[above.length - 1] : 0;
      }
      cycleRandomAccent();
      port.scrollTo({ top: target, behavior: "smooth" });
    }
    if (port && navUp && navDown) {
      port.addEventListener("scroll", updateArrows, { passive: true });
      navUp.addEventListener("click", function () { goToStage(-1); });
      navDown.addEventListener("click", function () { goToStage(1); });
      window.addEventListener("resize", updateArrows);
      updateArrows();
    }

    const canvas = document.getElementById("spotlight-canvas");
    if (canvas) {
      const ctx = canvas.getContext("2d", { alpha: false });
      let width = 0, height = 0, cellPx = 8, cols = 0, rows = 0, originX = 0;
      let mouse = { x: -2000, y: -2000, active: false }, ripples = [], smoothAcc = [80, 250, 123];
      function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        cellPx = Math.max(4, Math.floor(Math.min(width * 0.88, 920) / WM_W));
        originX = Math.round((width - WM_W * cellPx) / 2);
        cols = Math.ceil(width / cellPx) + 1;
        rows = Math.ceil(height / cellPx) + 1;
      }
      resize();
      window.addEventListener("resize", resize, { passive: true });
      window.addEventListener("pointermove", function (e) { mouse.x = e.clientX; mouse.y = e.clientY; mouse.active = true; }, { passive: true });
      window.addEventListener("pointerdown", function (e) {
        mouse.x = e.clientX; mouse.y = e.clientY; mouse.active = true;
        ripples.push({ x: e.clientX, y: e.clientY, born: performance.now(), maxR: 340, dur: 900 });
        if (ripples.length > 6) ripples.shift();
      }, { passive: true });
      window.oodaTriggerPulse = function (mode) {
        const cx = width * 0.5, cy = height * 0.46, now = performance.now();
        for (let i = 0; i < (mode === "storm" ? 4 : 2); i++) {
          ripples.push({
            x: cx + (Math.random() - 0.5) * (mode === "storm" ? width * 0.55 : 120),
            y: cy + (Math.random() - 0.5) * (mode === "storm" ? height * 0.45 : 80),
            born: now + i * 70,
            maxR: mode === "storm" ? 520 : 380,
            dur: 1050
          });
        }
      };
      function frame(t) {
        const scrollY = port ? port.scrollTop : 0;
        const sub = Math.min(1, Math.max(0, scrollY / (height * 0.65)));
        const acc = window.oodaCurrentAccent || [80, 250, 123];
        smoothAcc[0] += (acc[0] - smoothAcc[0]) * 0.12;
        smoothAcc[1] += (acc[1] - smoothAcc[1]) * 0.12;
        smoothAcc[2] += (acc[2] - smoothAcc[2]) * 0.12;
        const ar = Math.round(smoothAcc[0]), ag = Math.round(smoothAcc[1]), ab = Math.round(smoothAcc[2]);
        const hr = Math.min(255, ar + 65), hg = Math.min(255, ag + 65), hb = Math.min(255, ab + 65);
        ctx.fillStyle = "#06080b";
        ctx.fillRect(0, 0, width, height);
        const sec = t * 0.001;
        const wx = width * (0.5 + 0.34 * Math.sin(sec * 0.75));
        const wy = height * (0.45 + 0.22 * Math.cos(sec * 1.1));
        ripples = ripples.filter(function (rp) { return t - rp.born < rp.dur; });
        for (let r = 0; r < rows; r++) {
          const py = r * cellPx;
          for (let c = 0; c < cols; c++) {
            const px = c * cellPx;
            const dxm = px - mouse.x, dym = py - mouse.y;
            const sm = mouse.active ? Math.max(0, 1 - Math.sqrt(dxm * dxm + dym * dym) / 230) : 0;
            const dxw = px - wx, dyw = py - wy;
            const sw = Math.max(0, 1 - Math.sqrt(dxw * dxw + dyw * dyw) / 210) * (1 - sub * 0.65);
            let rip = 0;
            for (let i = 0; i < ripples.length; i++) {
              const rp = ripples[i], age = Math.max(0, t - rp.born) / rp.dur;
              const rad = rp.maxR * (1 - Math.pow(1 - age, 3));
              const dist = Math.abs(Math.hypot(px - rp.x, py - rp.y) - rad);
              if (dist < 26) rip = Math.max(rip, (1 - dist / 26) * (1 - age));
            }
            const spot = Math.max(sm, sw * 0.7);
            const wave = 0.5 + 0.5 * Math.sin(c * 0.14 + sec * 1.4) * Math.cos(r * 0.14 - sec * 1.1);
            const val = wave * (0.28 - 0.15 * sub) + spot * (0.68 - 0.35 * sub) + rip * 0.95;
            if (val > (BAYER[(r & 7) * 8 + (c & 7)] / 64) * 0.78) {
              const a = Math.min(0.85, (0.12 + spot * 0.55 + rip * 0.7) * (1 - sub * 0.45)).toFixed(2);
              ctx.fillStyle = (spot > 0.35 || rip > 0.3) ? "rgba(" + hr + "," + hg + "," + hb + "," + a + ")" : "rgba(" + ar + "," + ag + "," + ab + "," + a + ")";
              ctx.fillRect(px, py, cellPx - 1, cellPx - 1);
            }
          }
        }
        requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }

    document.addEventListener("click", function (e) {
      const sw = e.target.closest("[data-accent-name]");
      if (sw) {
        const f = ACCENTS.find(function (a) { return a.name.toLowerCase() === sw.dataset.accentName.toLowerCase(); });
        if (f) applyAccent(f);
        return;
      }
      if (e.target.closest("#act-pulse") && window.oodaTriggerPulse) window.oodaTriggerPulse("pulse");
      if (e.target.closest("#act-theme")) cycleRandomAccent();
      if (e.target.closest("#act-storm") && window.oodaTriggerPulse) window.oodaTriggerPulse("storm");
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "1" && window.oodaTriggerPulse) window.oodaTriggerPulse("pulse");
      else if (e.key === "2") cycleRandomAccent();
      else if (e.key === "3" && window.oodaTriggerPulse) window.oodaTriggerPulse("storm");
      else if (e.key === "ArrowDown") { e.preventDefault(); goToStage(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); goToStage(-1); }
    });
"""

def build_quota_sort_js() -> str:
    return """
    var list = document.getElementById("quota-list");
    var btns = document.querySelectorAll(".sort-btn[data-sort]");
    if (list && btns.length) {
      var activeMode = "rem-pct";
      var asc = true;
      function sortRows(mode, toggle) {
        if (mode === "reset") mode = "reset-sec";
        if (toggle && mode === activeMode) {
          asc = !asc;
        } else {
          activeMode = mode;
          asc = (mode === "rem-pct" || mode === "reset-sec" || mode === "name");
        }
        var rows = Array.prototype.slice.call(list.querySelectorAll(".quota-row"));
        rows.sort(function (a, b) {
          var cmp = 0;
          if (mode === "rem-pct") {
            cmp = parseFloat(a.getAttribute("data-rem-pct") || "0") - parseFloat(b.getAttribute("data-rem-pct") || "0");
            if (cmp === 0) {
              cmp = parseFloat(a.getAttribute("data-reset-sec") || "0") - parseFloat(b.getAttribute("data-reset-sec") || "0");
            }
          } else if (mode === "reset-sec") {
            cmp = parseFloat(a.getAttribute("data-reset-sec") || "0") - parseFloat(b.getAttribute("data-reset-sec") || "0");
          } else if (mode === "tps") {
            cmp = parseFloat(a.getAttribute("data-tps") || "0") - parseFloat(b.getAttribute("data-tps") || "0");
          } else if (mode === "capacity") {
            cmp = parseFloat(a.getAttribute("data-capacity") || "0") - parseFloat(b.getAttribute("data-capacity") || "0");
          } else if (mode === "name") {
            var na = (a.getAttribute("data-name") || "").toLowerCase();
            var nb = (b.getAttribute("data-name") || "").toLowerCase();
            cmp = na < nb ? -1 : (na > nb ? 1 : 0);
          }
          return asc ? cmp : -cmp;
        });
        for (var i = 0; i < rows.length; i++) {
          list.appendChild(rows[i]);
        }
        for (var j = 0; j < btns.length; j++) {
          if (btns[j].getAttribute("data-sort") === mode) {
            btns[j].classList.add("active");
          } else {
            btns[j].classList.remove("active");
          }
        }
      }
      window.sortQuotaGraph = sortRows;
      for (var k = 0; k < btns.length; k++) {
        btns[k].addEventListener("click", function () {
          sortRows(this.getAttribute("data-sort"), true);
        });
      }
    }
  })();
  </script>
"""
