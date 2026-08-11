"""Document portal hero + lakehouse visual + instructors + TOC."""

import streamlit as st
import streamlit.components.v1 as components

from content.course import COURSE
from content.home import HOME_HERO_BADGES, HOME_TECH_STRIP
from content.instructors import INSTRUCTORS
from utils.whatsapp import WHATSAPP_CONTACTS


TOC_ITEMS = [
    ("#sec-mentors", "00", "Mentors"),
    ("#sec-info", "01", "Info"),
    ("#sec-plan", "02", "Plan"),
    ("#sec-syllabus", "03", "Syllabus"),
    ("#sec-highlights", "04", "Why"),
    ("#sec-interview", "05", "Interview"),
    ("#sec-tools", "06", "Tools"),
    ("#sec-coming", "07", "Soon"),
    ("#sec-join", "08", "Join"),
]


def _lakehouse_hero_html() -> str:
    """Unique medallion lakehouse theater — not a basic linear ETL strip."""
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
    font-family: Segoe UI, Outfit, sans-serif;
    background: transparent;
    color: #F8FAFC;
  }
  .theater {
    position: relative;
    overflow: hidden;
    border-radius: 18px;
    border: 1px solid rgba(0,164,239,0.3);
    min-height: 280px;
    padding: 14px 12px 12px;
    background:
      radial-gradient(ellipse 60% 50% at 50% 45%, rgba(0,120,212,0.22), transparent 60%),
      linear-gradient(165deg, #070b16 0%, #0b1220 55%, #080d18 100%);
  }
  .grid {
    position: absolute; inset: 0; opacity: 0.35; pointer-events: none;
    background-image:
      linear-gradient(rgba(0,164,239,0.07) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,164,239,0.07) 1px, transparent 1px);
    background-size: 28px 28px;
    mask-image: radial-gradient(ellipse at center, black 20%, transparent 75%);
  }
  .topbar {
    position: relative; z-index: 3;
    display: flex; justify-content: space-between; align-items: center;
    gap: 8px; flex-wrap: wrap; margin-bottom: 6px;
  }
  .live {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 10px; font-weight: 800; letter-spacing: 0.14em; color: #86efac;
  }
  .dot {
    width: 7px; height: 7px; border-radius: 50%; background: #22c55e;
    box-shadow: 0 0 0 0 rgba(34,197,94,.5);
    animation: pulse 1.5s ease-out infinite;
  }
  .metrics { display: flex; gap: 6px; flex-wrap: wrap; }
  .metric {
    font-size: 10px; font-weight: 700; color: #7DD3FC;
    padding: 4px 8px; border-radius: 999px;
    border: 1px solid rgba(0,164,239,0.28);
    background: rgba(15,23,42,0.75);
  }
  .metric b { color: #F8FAFC; }
  .stage {
    position: relative; z-index: 2;
    height: 190px; margin: 4px 0 8px;
  }
  .ring {
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 1px dashed rgba(148,163,184,0.25);
  }
  .r1 { width: 110px; height: 110px; border-color: rgba(205,127,50,0.45); }
  .r2 { width: 160px; height: 160px; border-color: rgba(148,163,184,0.35); }
  .r3 { width: 210px; height: 210px; border-color: rgba(234,179,8,0.35); }
  .core {
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    width: 78px; height: 78px; border-radius: 50%;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    text-align: center;
    background: radial-gradient(circle at 30% 30%, rgba(0,164,239,0.45), #0b1220 70%);
    border: 1px solid rgba(0,164,239,0.55);
    box-shadow: 0 0 40px rgba(0,120,212,0.35);
    animation: corePulse 3.5s ease-in-out infinite;
  }
  .core .cloud { font-size: 18px; line-height: 1; }
  .core .t1 { font-size: 9px; font-weight: 800; letter-spacing: 0.12em; margin-top: 2px; }
  .core .t2 { font-size: 8px; color: #94A3B8; letter-spacing: 0.04em; }
  .layer {
    position: absolute; left: 50%; font-size: 9px; font-weight: 800;
    letter-spacing: 0.08em; padding: 3px 8px; border-radius: 999px;
    transform: translateX(-50%);
  }
  .bronze { top: 8px; color: #fdba74; background: rgba(154,52,18,0.25); border: 1px solid rgba(251,146,60,0.35); }
  .silver { top: 36px; color: #e2e8f0; background: rgba(71,85,105,0.35); border: 1px solid rgba(148,163,184,0.35); }
  .gold { bottom: 6px; color: #fde68a; background: rgba(161,98,7,0.28); border: 1px solid rgba(234,179,8,0.35); }
  .orbit {
    position: absolute; left: 50%; top: 50%;
    width: 0; height: 0;
  }
  .o1 { animation: spin 14s linear infinite; }
  .o2 { animation: spin 18s linear infinite reverse; }
  .o3 { animation: spin 22s linear infinite; }
  .sat {
    position: absolute; width: 52px; height: 52px; margin: -26px 0 0 -26px;
    border-radius: 14px; display: grid; place-items: center;
    font-size: 10px; font-weight: 800; color: #fff;
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 8px 20px rgba(0,0,0,0.35);
  }
  .sat small {
    display: block; font-size: 8px; font-weight: 600; opacity: 0.9; margin-top: 1px;
  }
  .adf { background: linear-gradient(145deg,#0078D4,#00A4EF); top: -78px; left: 0; }
  .spark { background: linear-gradient(145deg,#E25A1C,#f97316); top: 0; left: 88px; }
  .dbx { background: linear-gradient(145deg,#FF3621,#ff6b5a); top: 78px; left: 0; }
  .sql { background: linear-gradient(145deg,#CC2927,#f24c4a); top: 0; left: -88px; }
  .particle {
    position: absolute; width: 5px; height: 5px; border-radius: 50%;
    background: #22D3EE; box-shadow: 0 0 8px #22D3EE;
    left: 50%; top: 50%;
  }
  .p1 { animation: shoot 2.8s linear infinite; }
  .p2 { animation: shoot 2.8s linear infinite 0.9s; background:#A78BFA; box-shadow:0 0 8px #A78BFA; }
  .p3 { animation: shoot 2.8s linear infinite 1.7s; background:#FBBF24; box-shadow:0 0 8px #FBBF24; }
  .footer {
    position: relative; z-index: 3;
    display: flex; justify-content: space-between; align-items: center; gap: 8px; flex-wrap: wrap;
  }
  .caption { font-size: 11px; color: #94A3B8; letter-spacing: 0.03em; }
  .chip {
    font-size: 10px; font-weight: 700; color: #E0F2FE;
    padding: 4px 8px; border-radius: 999px;
    background: rgba(0,120,212,0.18); border: 1px solid rgba(0,164,239,0.28);
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  @keyframes corePulse {
    0%,100% { box-shadow: 0 0 28px rgba(0,120,212,0.28); }
    50% { box-shadow: 0 0 48px rgba(0,164,239,0.5); }
  }
  @keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(34,197,94,.5); }
    70% { box-shadow: 0 0 0 8px rgba(34,197,94,0); }
    100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
  }
  @keyframes shoot {
    0% { transform: translate(-50%, -50%) scale(0.6); opacity: 0; }
    15% { opacity: 1; }
    100% { transform: translate(calc(-50% + 70px), calc(-50% - 55px)) scale(1); opacity: 0; }
  }
  @media (max-width: 420px) {
    .stage { height: 170px; }
    .r3 { width: 170px; height: 170px; }
    .r2 { width: 130px; height: 130px; }
    .adf { top: -64px; } .dbx { top: 64px; }
    .spark { left: 72px; } .sql { left: -72px; }
    .sat { width: 46px; height: 46px; margin: -23px 0 0 -23px; font-size: 9px; }
  }
</style>
</head>
<body>
  <div class="theater">
    <div class="grid"></div>
    <div class="topbar">
      <div class="live"><span class="dot"></span> LIVE LAKEHOUSE</div>
      <div class="metrics">
        <div class="metric">Ingest <b>2.4k/s</b></div>
        <div class="metric">Jobs <b>12</b></div>
        <div class="metric">Quality <b>99.2%</b></div>
      </div>
    </div>
    <div class="stage">
      <div class="ring r3"></div>
      <div class="ring r2"></div>
      <div class="ring r1"></div>
      <div class="layer bronze">BRONZE</div>
      <div class="layer silver">SILVER</div>
      <div class="layer gold">GOLD</div>
      <div class="core">
        <div class="cloud">☁️</div>
        <div class="t1">AZURE</div>
        <div class="t2">LAKEHOUSE</div>
      </div>
      <div class="orbit o1">
        <div class="sat adf">ADF<small>Orchestrate</small></div>
      </div>
      <div class="orbit o2">
        <div class="sat spark">SPARK<small>Transform</small></div>
        <div class="sat sql">SQL<small>Model</small></div>
      </div>
      <div class="orbit o3">
        <div class="sat dbx">DBX<small>Compute</small></div>
      </div>
      <span class="particle p1"></span>
      <span class="particle p2"></span>
      <span class="particle p3"></span>
    </div>
    <div class="footer">
      <div class="caption">Medallion Architecture · Streaming data into trusted gold layer</div>
      <div class="chip">Unique DE Visual</div>
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
    """Program title + unique lakehouse medallion animation."""
    st.markdown(
        """
        <section class="program-banner" aria-label="Program overview">
          <div class="program-banner-head">
            <div class="program-kicker">Official Curriculum</div>
            <h2 class="program-title">Azure Data Engineering Master Program</h2>
            <p class="program-sub">
              Learn the real lakehouse way — Bronze · Silver · Gold with ADF, Spark, Databricks &amp; SQL
            </p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    components.html(_lakehouse_hero_html(), height=320, scrolling=False)


def render_instructors() -> None:
    """Mentor / instructor spotlight cards."""
    cards = []
    for person in INSTRUCTORS:
        accent = person.get("accent", "azure")
        cards.append(
            f"""
            <div class="mentor-card mentor-{accent}">
              <div class="mentor-avatar">{person['initials']}</div>
              <div class="mentor-body">
                <div class="mentor-name">{person['name']}</div>
                <div class="mentor-role">{person['role']}</div>
                <div class="mentor-exp">{person['experience']}</div>
                <p class="mentor-focus">{person['focus']}</p>
              </div>
            </div>
            """
        )
    st.markdown(
        f"""
        <section id="sec-mentors" class="mentor-section">
          <div class="mentor-head">
            <div class="program-kicker">Learn from Industry Mentors</div>
            <h3 class="mentor-title">Instructor Details</h3>
            <p class="mentor-sub">Guided by practitioners with decades of hands-on data engineering experience.</p>
          </div>
          <div class="mentor-grid">
            {''.join(cards)}
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


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
