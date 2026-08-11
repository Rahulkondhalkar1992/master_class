"""Home hero visual — mobile-first badges and lighter motion."""

import streamlit as st

from content.course import COURSE
from content.home import HOME_HERO_BADGES, HOME_TECH_STRIP


def render_hero() -> None:
    badges = "".join(f'<span class="hero-badge">{b}</span>' for b in HOME_HERO_BADGES)
    tech = " · ".join(HOME_TECH_STRIP)
    st.markdown(
        f"""
        <div class="hero-wrap">
          <div class="hero-content">
            <div class="hero-eyebrow">☁️ Azure Learnings Academy</div>
            <h1 class="hero-title">
              <span class="gradient-text">{COURSE['name']}</span>
            </h1>
            <div class="hero-badges">{badges}</div>
            <p class="hero-subtitle">{COURSE['tagline']}</p>
            <div class="hero-tech-strip">{tech}</div>
          </div>
          <div class="hero-network desktop-only-motion">
            <div class="tech-orbit">
              <div class="tech-pill">ADF</div>
              <div class="tech-pill">DATABRICKS</div>
              <div class="tech-pill">PYSPARK</div>
              <div class="tech-pill">SQL</div>
              <div class="tech-pill">PYTHON</div>
              <div class="tech-pill">GITHUB</div>
              <div class="tech-pill">DATA LAKE</div>
              <div class="tech-pill">SYNAPSE</div>
            </div>
            <div class="hero-core">
              <div class="core-icon">☁️</div>
              <div class="core-title">AZURE</div>
              <div class="core-sub">DATA ENGINEERING</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_mobile_quick_nav() -> None:
    """Sticky compact quick navigation for mobile (query-param links)."""
    st.markdown(
        """
        <nav class="mqn-sticky" aria-label="Mobile quick navigation">
          <a class="mqn-btn" href="?nav=syllabus">📚 Syllabus</a>
          <a class="mqn-btn" href="?nav=roadmap">🗺️ Roadmap</a>
          <a class="mqn-btn" href="?nav=interview">🎯 Interview</a>
          <a class="mqn-btn mqn-primary" href="?nav=enquiry">🚀 Join Now</a>
        </nav>
        """,
        unsafe_allow_html=True,
    )
