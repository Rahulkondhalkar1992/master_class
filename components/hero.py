"""Document portal hero + sticky TOC + mobile action dock."""

import streamlit as st

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

# Brand-colored SVG marks (inline — no external logo downloads)
ICON_ADF = """
<svg viewBox="0 0 48 48" class="etl-svg" aria-hidden="true">
  <rect x="4" y="8" width="16" height="12" rx="2" fill="#0078D4"/>
  <rect x="28" y="8" width="16" height="12" rx="2" fill="#50E6FF"/>
  <rect x="16" y="28" width="16" height="12" rx="2" fill="#005A9E"/>
  <path d="M20 14h8M24 14v14" stroke="#F8FAFC" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="12" cy="14" r="2" fill="#fff"/><circle cx="36" cy="14" r="2" fill="#003A6C"/>
</svg>
"""

ICON_DATABRICKS = """
<svg viewBox="0 0 48 48" class="etl-svg" aria-hidden="true">
  <path d="M8 34 L24 10 L40 34 Z" fill="#FF3621"/>
  <path d="M14 34 L24 18 L34 34 Z" fill="#FF6B5A"/>
  <rect x="20" y="30" width="8" height="8" rx="1" fill="#FFFFFF"/>
  <path d="M10 38h28" stroke="#FF3621" stroke-width="2.5" stroke-linecap="round"/>
</svg>
"""

ICON_SQL = """
<svg viewBox="0 0 48 48" class="etl-svg" aria-hidden="true">
  <ellipse cx="24" cy="12" rx="14" ry="6" fill="#CC2927"/>
  <path d="M10 12v18c0 3.3 6.3 6 14 6s14-2.7 14-6V12" fill="#A52321"/>
  <ellipse cx="24" cy="12" rx="14" ry="6" fill="#F24C4A"/>
  <ellipse cx="24" cy="20" rx="14" ry="5" fill="none" stroke="#FF8A88" stroke-width="1.5"/>
  <ellipse cx="24" cy="28" rx="14" ry="5" fill="none" stroke="#FF8A88" stroke-width="1.5"/>
  <text x="24" y="27" text-anchor="middle" fill="#fff" font-size="9" font-weight="700" font-family="Arial">SQL</text>
</svg>
"""

ICON_SPARK = """
<svg viewBox="0 0 48 48" class="etl-svg" aria-hidden="true">
  <circle cx="24" cy="24" r="5" fill="#E25A1C"/>
  <g stroke="#E25A1C" stroke-width="3.2" stroke-linecap="round">
    <path d="M24 6v8M24 34v8M6 24h8M34 24h8"/>
    <path d="M11 11l6 6M31 31l6 6M37 11l-6 6M17 31l-6 6"/>
  </g>
  <circle cx="24" cy="24" r="2.5" fill="#FFD2B8"/>
</svg>
"""

ICON_LAKE = """
<svg viewBox="0 0 48 48" class="etl-svg" aria-hidden="true">
  <path d="M8 20c4-8 12-10 16-10s12 2 16 10c-2 10-8 18-16 18S10 30 8 20z" fill="#0078D4"/>
  <path d="M12 22c3-5 8-7 12-7s9 2 12 7" fill="none" stroke="#50E6FF" stroke-width="2"/>
  <path d="M14 28c2 4 5 6 10 6s8-2 10-6" fill="none" stroke="#9FEAF9" stroke-width="1.8"/>
</svg>
"""

ICON_SOURCE = """
<svg viewBox="0 0 48 48" class="etl-svg" aria-hidden="true">
  <rect x="8" y="10" width="32" height="28" rx="4" fill="#334155"/>
  <rect x="12" y="14" width="24" height="4" rx="1" fill="#22D3EE"/>
  <rect x="12" y="22" width="18" height="3" rx="1" fill="#64748B"/>
  <rect x="12" y="28" width="14" height="3" rx="1" fill="#64748B"/>
  <circle cx="34" cy="30" r="5" fill="#22C55E"/>
</svg>
"""


def _etl_node(name: str, label: str, icon_svg: str, delay: str = "0s") -> str:
    return f"""
    <div class="etl-node etl-{name}" style="--d:{delay}">
      <div class="etl-icon">{icon_svg}</div>
      <div class="etl-label">{label}</div>
      <div class="etl-pulse"></div>
    </div>
    """


def _etl_pipe(delay: str = "0s") -> str:
    return f"""
    <div class="etl-pipe" style="--d:{delay}">
      <span class="etl-packet"></span>
      <span class="etl-packet p2"></span>
      <span class="etl-packet p3"></span>
    </div>
    """


def render_etl_animation() -> str:
    """Live ETL / loading pipeline for the hero."""
    return f"""
    <div class="etl-stage" aria-label="Animated data engineering ETL pipeline">
      <div class="etl-live">
        <span class="etl-live-dot"></span> LIVE ETL FLOW
      </div>
      <div class="etl-track">
        {_etl_node("source", "Source", ICON_SOURCE, "0s")}
        {_etl_pipe("0s")}
        {_etl_node("adf", "Azure ADF", ICON_ADF, "0.2s")}
        {_etl_pipe("0.35s")}
        {_etl_node("lake", "Data Lake", ICON_LAKE, "0.45s")}
        {_etl_pipe("0.55s")}
        {_etl_node("spark", "Apache Spark", ICON_SPARK, "0.7s")}
        {_etl_pipe("0.85s")}
        {_etl_node("dbx", "Databricks", ICON_DATABRICKS, "1s")}
        {_etl_pipe("1.1s")}
        {_etl_node("sql", "SQL", ICON_SQL, "1.25s")}
      </div>
      <div class="etl-caption">
        Ingest → Orchestrate → Store → Transform → Analyze
      </div>
      <div class="etl-status">
        <span class="etl-bar"><i></i></span>
        <span class="etl-status-text">Pipeline running · batches loading…</span>
      </div>
    </div>
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
    """Clean program title + animated ETL visual above the chapter TOC."""
    etl = render_etl_animation()
    st.markdown(
        f"""
        <section class="program-banner" aria-label="Program overview">
          <div class="program-banner-head">
            <div class="program-kicker">Official Curriculum</div>
            <h2 class="program-title">Azure Data Engineering Master Program</h2>
            <p class="program-sub">
              A live, practical learning path across ADF · Databricks · Spark · SQL · Delta Lake
            </p>
          </div>
          <div class="program-visual">
            {etl}
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
