"""Document portal hero + sticky TOC + mobile action dock."""

import streamlit as st
import streamlit.components.v1 as components

from content.course import COURSE
from content.home import HOME_HERO_BADGES, HOME_TECH_STRIP
from utils.whatsapp import WHATSAPP_CONTACTS


TOC_ITEMS = [
    ("#sec-info", "01", "Info"),
    ("#sec-plan", "02", "Plan"),
    ("#sec-syllabus", "03", "Syllabus"),
    ("#sec-highlights", "04", "Why"),
    ("#sec-interview", "05", "Interview"),
    ("#sec-tools", "06", "Tools"),
    ("#sec-coming", "07", "Soon"),
    ("#sec-join", "08", "Join"),
]


def _etl_iframe_html() -> str:
    """Self-contained HTML for components.html (avoids Streamlit markdown sanitizer)."""
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: Outfit, Segoe UI, sans-serif;
    background: transparent;
    color: #F8FAFC;
  }
  .stage {
    border: 1px solid rgba(0,164,239,0.28);
    border-radius: 14px;
    padding: 12px 10px 10px;
    background: linear-gradient(180deg, rgba(8,16,32,0.98), rgba(11,17,32,0.92));
  }
  .live {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 11px; font-weight: 750; letter-spacing: 0.12em; color: #86efac;
    margin-bottom: 10px;
  }
  .dot {
    width: 8px; height: 8px; border-radius: 50%; background: #22c55e;
    animation: blink 1.6s ease-out infinite;
  }
  @keyframes blink {
    0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.55); }
    70% { box-shadow: 0 0 0 8px rgba(34,197,94,0); }
    100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
  }
  .track {
    display: flex; align-items: center; gap: 2px;
    overflow-x: auto; padding-bottom: 4px; scrollbar-width: none;
  }
  .track::-webkit-scrollbar { display: none; }
  .node { flex: 0 0 auto; width: 72px; text-align: center; }
  .icon {
    width: 54px; height: 54px; margin: 0 auto; border-radius: 14px;
    display: grid; place-items: center; font-size: 11px; font-weight: 800;
    letter-spacing: 0.02em; color: #fff;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 8px 18px rgba(0,0,0,0.28);
    animation: floaty 3s ease-in-out infinite;
  }
  .node:nth-child(1) .icon { animation-delay: 0s; background: linear-gradient(145deg,#334155,#1e293b); }
  .node:nth-child(3) .icon { animation-delay: .2s; background: linear-gradient(145deg,#0078D4,#00A4EF); }
  .node:nth-child(5) .icon { animation-delay: .4s; background: linear-gradient(145deg,#0ea5e9,#0284c7); }
  .node:nth-child(7) .icon { animation-delay: .6s; background: linear-gradient(145deg,#E25A1C,#f97316); }
  .node:nth-child(9) .icon { animation-delay: .8s; background: linear-gradient(145deg,#FF3621,#ff6b5a); }
  .node:nth-child(11) .icon { animation-delay: 1s; background: linear-gradient(145deg,#CC2927,#f24c4a); }
  .label {
    margin-top: 6px; font-size: 10px; font-weight: 700; color: #CBD5E1; white-space: nowrap;
  }
  .pipe {
    position: relative; flex: 0 0 22px; height: 4px; margin-bottom: 18px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(0,164,239,.2), rgba(34,211,238,.7), rgba(0,164,239,.2));
    overflow: hidden;
  }
  .pkt {
    position: absolute; top: -2px; left: -8px; width: 9px; height: 8px; border-radius: 999px;
    background: #22D3EE; box-shadow: 0 0 8px #22D3EE;
    animation: flow 1.8s linear infinite;
  }
  .pkt.b { animation-delay: .6s; background: #00A4EF; }
  .pkt.c { animation-delay: 1.2s; background: #A78BFA; }
  @keyframes flow {
    0% { left: -10px; opacity: 0; }
    15% { opacity: 1; }
    85% { opacity: 1; }
    100% { left: calc(100% + 4px); opacity: 0; }
  }
  @keyframes floaty {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-3px); }
  }
  .caption {
    text-align: center; font-size: 11px; color: #94A3B8; margin-top: 8px; letter-spacing: 0.03em;
  }
  .status {
    display: flex; align-items: center; gap: 8px; margin-top: 8px;
    padding: 6px 8px; border-radius: 10px;
    background: rgba(0,120,212,0.12); border: 1px solid rgba(0,164,239,0.2);
  }
  .bar {
    flex: 1; height: 6px; border-radius: 999px; background: rgba(148,163,184,0.2); overflow: hidden;
  }
  .bar span {
    display: block; height: 100%; width: 42%; border-radius: 999px;
    background: linear-gradient(90deg,#0078D4,#22D3EE,#0078D4);
    animation: load 1.4s ease-in-out infinite;
  }
  @keyframes load {
    0% { transform: translateX(-120%); }
    100% { transform: translateX(280%); }
  }
  .status-text { font-size: 10px; color: #7DD3FC; font-weight: 600; white-space: nowrap; }
</style>
</head>
<body>
  <div class="stage">
    <div class="live"><span class="dot"></span> LIVE ETL FLOW</div>
    <div class="track">
      <div class="node"><div class="icon">SRC</div><div class="label">Source</div></div>
      <div class="pipe"><span class="pkt"></span><span class="pkt b"></span><span class="pkt c"></span></div>
      <div class="node"><div class="icon">ADF</div><div class="label">Azure ADF</div></div>
      <div class="pipe"><span class="pkt"></span><span class="pkt b"></span><span class="pkt c"></span></div>
      <div class="node"><div class="icon">LAKE</div><div class="label">Data Lake</div></div>
      <div class="pipe"><span class="pkt"></span><span class="pkt b"></span><span class="pkt c"></span></div>
      <div class="node"><div class="icon">SPARK</div><div class="label">Apache Spark</div></div>
      <div class="pipe"><span class="pkt"></span><span class="pkt b"></span><span class="pkt c"></span></div>
      <div class="node"><div class="icon">DBX</div><div class="label">Databricks</div></div>
      <div class="pipe"><span class="pkt"></span><span class="pkt b"></span><span class="pkt c"></span></div>
      <div class="node"><div class="icon">SQL</div><div class="label">SQL</div></div>
    </div>
    <div class="caption">Ingest → Orchestrate → Store → Transform → Analyze</div>
    <div class="status">
      <div class="bar"><span></span></div>
      <div class="status-text">Pipeline running · batches loading…</div>
    </div>
  </div>
</body>
</html>
"""


def render_hero() -> None:
    badges = "".join(f'<span class="hero-badge">{b}</span>' for b in HOME_HERO_BADGES)
    tech_pills = "".join(f"<span>{t}</span>" for t in HOME_TECH_STRIP)
    st.markdown(
        f"""
        <header class="doc-hero" id="top">
          <div class="doc-hero-glow"></div>
          <div class="doc-hero-glow doc-hero-glow-2"></div>
          <div class="doc-hero-grid"></div>
          <div class="doc-hero-inner">
            <div class="doc-kicker">☁️ Azure Learnings Academy</div>
            <div class="doc-mobile-eyebrow">Study Material Portal</div>
            <h1 class="doc-hero-title">
              <span class="gradient-text">{COURSE['name']}</span>
            </h1>
            <p class="doc-hero-lead">{COURSE['tagline']}</p>
            <div class="hero-badges">{badges}</div>
            <div class="hero-tech-pills mobile-tech-rail">{tech_pills}</div>
            <div class="mobile-hero-cta">
              <a class="mhc-btn mhc-primary" href="#sec-plan" target="_self">🗓️ 90-Day Plan</a>
              <a class="mhc-btn" href="#sec-syllabus" target="_self">📚 Syllabus</a>
              <a class="mhc-btn mhc-join" href="#sec-join" target="_self">🚀 Join</a>
            </div>
          </div>
        </header>
        """,
        unsafe_allow_html=True,
    )


def render_program_banner() -> None:
    """Clean program title + iframe ETL animation (renders correctly in Streamlit)."""
    st.markdown(
        """
        <section class="program-banner" aria-label="Program overview">
          <div class="program-banner-head">
            <div class="program-kicker">Official Curriculum</div>
            <h2 class="program-title">Azure Data Engineering Master Program</h2>
            <p class="program-sub">
              A live, practical learning path across ADF · Databricks · Spark · SQL · Delta Lake
            </p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    components.html(_etl_iframe_html(), height=210, scrolling=False)


def render_toc() -> None:
    links = "".join(
        f'<a class="toc-chip" href="{href}" target="_self"><span class="toc-num">{num}</span>{label}</a>'
        for href, num, label in TOC_ITEMS
    )
    st.markdown(
        f"""
        <nav class="doc-toc sticky-toc" aria-label="Document contents">
          <div class="toc-head">
            <div class="toc-title">Jump to chapter</div>
            <a class="toc-join" href="#sec-join" target="_self">Join →</a>
          </div>
          <div class="toc-row">{links}</div>
        </nav>
        """,
        unsafe_allow_html=True,
    )


def render_mobile_dock() -> None:
    """Fixed bottom action dock — mobile primary navigation."""
    wa = WHATSAPP_CONTACTS[0]["url"]
    st.markdown(
        f"""
        <nav class="mobile-dock" aria-label="Mobile quick actions">
          <a class="dock-item" href="#sec-plan" target="_self">
            <span class="dock-ico">🗓️</span><span>Plan</span>
          </a>
          <a class="dock-item" href="#sec-syllabus" target="_self">
            <span class="dock-ico">📚</span><span>Syllabus</span>
          </a>
          <a class="dock-item dock-wa" href="{wa}" target="_self" rel="noopener noreferrer">
            <span class="dock-ico">💬</span><span>WhatsApp</span>
          </a>
          <a class="dock-item dock-join" href="#sec-join" target="_self">
            <span class="dock-ico">🚀</span><span>Join</span>
          </a>
        </nav>
        <div class="mobile-dock-spacer"></div>
        """,
        unsafe_allow_html=True,
    )
