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
            <div class="doc-hero-visual" aria-hidden="true">
              <div class="doc-hero-core">
                <div class="core-icon">☁️</div>
                <div class="core-title">AZURE</div>
                <div class="core-sub">DATA ENGINEERING</div>
              </div>
              <div class="doc-hero-pills desktop-pills">
                <span>ADF</span><span>SQL</span><span>Databricks</span>
                <span>PySpark</span><span>Delta</span><span>Python</span>
              </div>
            </div>
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
