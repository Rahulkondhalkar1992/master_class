"""Document portal hero + linear lakehouse visual + instructors + TOC."""

import streamlit as st
import streamlit.components.v1 as components

from content.course import COURSE
from content.home import HOME_HERO_BADGES, HOME_TECH_STRIP
from content.instructors import INSTRUCTORS
from utils.whatsapp import WHATSAPP_CONTACTS


TOC_ITEMS = [
    ("#sec-info", "01", "Info"),
    ("#sec-plan", "02", "Plan"),
    ("#sec-syllabus", "03", "Syllabus"),
    ("#sec-highlights", "04", "Why"),
    ("#sec-interview", "05", "Interview"),
    ("#sec-tools", "06", "Tools"),
    ("#sec-coming", "07", "Soon"),
    ("#sec-mentors", "08", "Mentors"),
    ("#sec-join", "09", "Join"),
]


def _linear_pipeline_html() -> str:
    """Linear medallion conveyor — unique DE visual without orbital motion."""
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: Segoe UI, sans-serif;
    background: transparent;
    color: #F8FAFC;
  }
  .board {
    border-radius: 16px;
    border: 1px solid rgba(0,164,239,0.28);
    padding: 12px 10px 10px;
    background:
      linear-gradient(180deg, rgba(8,14,28,0.98), rgba(11,17,32,0.94));
    overflow: hidden;
  }
  .head {
    display: flex; justify-content: space-between; align-items: center;
    gap: 8px; flex-wrap: wrap; margin-bottom: 10px;
  }
  .live {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 10px; font-weight: 800; letter-spacing: 0.12em; color: #86efac;
  }
  .dot {
    width: 7px; height: 7px; border-radius: 50%; background: #22c55e;
    animation: blink 1.5s ease-out infinite;
  }
  .tag {
    font-size: 10px; font-weight: 700; color: #7DD3FC;
    padding: 4px 8px; border-radius: 999px;
    border: 1px solid rgba(0,164,239,0.25);
    background: rgba(15,23,42,0.8);
  }
  .lanes {
    display: grid;
    grid-template-columns: 72px 1fr;
    gap: 8px;
  }
  .layer-col { display: flex; flex-direction: column; gap: 8px; }
  .layer {
    height: 46px; border-radius: 10px; display: grid; place-items: center;
    font-size: 10px; font-weight: 800; letter-spacing: 0.08em;
  }
  .bronze { background: rgba(154,52,18,0.35); color: #fdba74; border: 1px solid rgba(251,146,60,0.35); }
  .silver { background: rgba(71,85,105,0.4); color: #e2e8f0; border: 1px solid rgba(148,163,184,0.35); }
  .gold { background: rgba(161,98,7,0.32); color: #fde68a; border: 1px solid rgba(234,179,8,0.35); }
  .belt {
    position: relative;
    border-radius: 12px;
    border: 1px solid rgba(148,163,184,0.16);
    background: rgba(15,23,42,0.65);
    overflow: hidden;
    min-height: 154px;
    padding: 10px 8px;
  }
  .rail {
    position: absolute; left: 8px; right: 8px; height: 3px; border-radius: 999px;
    background: linear-gradient(90deg, rgba(0,164,239,0.15), rgba(34,211,238,0.55), rgba(0,164,239,0.15));
  }
  .rail.r1 { top: 30px; }
  .rail.r2 { top: 76px; }
  .rail.r3 { top: 122px; }
  .pack {
    position: absolute; width: 54px; height: 34px; border-radius: 10px;
    display: grid; place-items: center; font-size: 9px; font-weight: 800; color: #fff;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 6px 14px rgba(0,0,0,0.3);
  }
  .adf { background: linear-gradient(145deg,#0078D4,#00A4EF); top: 14px; animation: slide 4.5s linear infinite; }
  .spark { background: linear-gradient(145deg,#E25A1C,#f97316); top: 60px; animation: slide 5.2s linear infinite 0.6s; }
  .dbx { background: linear-gradient(145deg,#FF3621,#ff6b5a); top: 60px; animation: slide 5.2s linear infinite 2.2s; }
  .sql { background: linear-gradient(145deg,#CC2927,#f24c4a); top: 106px; animation: slide 4.8s linear infinite 1.1s; }
  .lake {
    position: absolute; right: 10px; top: 50%; transform: translateY(-50%);
    width: 58px; height: 58px; border-radius: 14px;
    display: grid; place-items: center; text-align: center;
    font-size: 9px; font-weight: 800; letter-spacing: 0.04em;
    background: radial-gradient(circle at 30% 30%, rgba(0,164,239,0.45), #0b1220 70%);
    border: 1px solid rgba(0,164,239,0.45);
    box-shadow: 0 0 24px rgba(0,120,212,0.3);
  }
  .lake span { display: block; font-size: 14px; margin-bottom: 2px; }
  .foot {
    margin-top: 8px; display: flex; justify-content: space-between; gap: 8px; flex-wrap: wrap;
    font-size: 11px; color: #94A3B8;
  }
  .status {
    display: flex; align-items: center; gap: 8px; min-width: 160px;
  }
  .bar {
    flex: 1; height: 5px; border-radius: 999px; background: rgba(148,163,184,0.2); overflow: hidden;
  }
  .bar i {
    display: block; width: 40%; height: 100%; border-radius: 999px;
    background: linear-gradient(90deg,#0078D4,#22D3EE);
    animation: load 1.3s ease-in-out infinite;
  }
  @keyframes slide {
    0% { left: 8px; opacity: 0; }
    8% { opacity: 1; }
    85% { opacity: 1; }
    100% { left: calc(100% - 78px); opacity: 0.15; }
  }
  @keyframes load {
    0% { transform: translateX(-120%); }
    100% { transform: translateX(280%); }
  }
  @keyframes blink {
    0% { box-shadow: 0 0 0 0 rgba(34,197,94,.5); }
    70% { box-shadow: 0 0 0 8px rgba(34,197,94,0); }
    100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
  }
</style>
</head>
<body>
  <div class="board">
    <div class="head">
      <div class="live"><span class="dot"></span> LIVE DATA PIPELINE</div>
      <div class="tag">Linear Medallion Flow</div>
    </div>
    <div class="lanes">
      <div class="layer-col">
        <div class="layer bronze">BRONZE</div>
        <div class="layer silver">SILVER</div>
        <div class="layer gold">GOLD</div>
      </div>
      <div class="belt">
        <div class="rail r1"></div>
        <div class="rail r2"></div>
        <div class="rail r3"></div>
        <div class="pack adf">ADF</div>
        <div class="pack spark">SPARK</div>
        <div class="pack dbx">DBX</div>
        <div class="pack sql">SQL</div>
        <div class="lake"><span>☁️</span>LAKE</div>
      </div>
    </div>
    <div class="foot">
      <div>Source → Ingest → Transform → Model → Trusted Gold</div>
      <div class="status"><div class="bar"><i></i></div>Processing…</div>
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
    """Program title + linear lakehouse pipeline animation."""
    st.markdown(
        """
        <section class="program-banner" aria-label="Program overview">
          <div class="program-banner-head">
            <div class="program-kicker">Official Curriculum</div>
            <h2 class="program-title">Azure Data Engineering Master Program</h2>
            <p class="program-sub">
              Linear medallion learning path — Bronze · Silver · Gold with ADF, Spark, Databricks &amp; SQL
            </p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    components.html(_linear_pipeline_html(), height=250, scrolling=False)


def render_instructors() -> None:
    """Mentor cards near contact — Streamlit-native only (avoids HTML text leakage)."""
    st.markdown('<div id="sec-mentors"></div>', unsafe_allow_html=True)
    st.markdown("### Learn from Industry Mentors")
    st.caption(
        "Instructor Details — guided by practitioners with decades of hands-on data engineering experience."
    )

    cols = st.columns(2)
    for col, person in zip(cols, INSTRUCTORS):
        with col:
            with st.container(border=True):
                st.markdown(f"#### {person['initials']}  ·  {person['name']}")
                st.markdown(f"**{person['role']}**")
                st.info(person["experience"])
                st.write(person["focus"])


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
