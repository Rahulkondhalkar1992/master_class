"""Home page — mobile-first order: Hero → Roadmap → Syllabus → marketing."""

import streamlit as st

from components.cards import render_cards
from components.hero import render_hero, render_mobile_quick_nav
from components.navbar import render_page_header, render_whatsapp_buttons
from content.course import COURSE
from content.home import (
    HOME_INTERVIEW,
    HOME_LIVE,
    HOME_ROADMAP_PREVIEW,
    HOME_SUPPORT,
    HOME_SYLLABUS_PREVIEW,
    HOME_TOOLS,
    HOME_WHY,
)
from utils.navigation import navigate_to
from utils.whatsapp import WHATSAPP_CONTACTS


def _handle_quick_nav() -> None:
    nav = st.query_params.get("nav")
    if not nav:
        return
    mapping = {
        "syllabus": ("syllabus", None),
        "roadmap": ("roadmap", None),
        "interview": ("syllabus", "interview_mod"),
        "enquiry": ("enquiry", None),
        "join": ("enquiry", None),
    }
    if nav in mapping:
        page, focus = mapping[nav]
        st.query_params.clear()
        navigate_to(st.session_state, page, syllabus_key=focus)
        st.rerun()


def _section_anchor(anchor_id: str, label: str, title: str) -> None:
    st.markdown(
        f"""
        <div id="{anchor_id}" class="home-section-head">
          <div class="section-label">{label}</div>
          <h2 class="home-section-title">{title}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_roadmap_preview() -> None:
    _section_anchor("home-roadmap", "Decision Section", "🚀 Learning Roadmap")
    st.caption("90-day practical path — ADF first, then SQL, modeling, Python, Databricks, and project.")

    steps_html = []
    for idx, title in enumerate(HOME_ROADMAP_PREVIEW):
        steps_html.append(f'<div class="home-road-step">{title}</div>')
        if idx < len(HOME_ROADMAP_PREVIEW) - 1:
            steps_html.append('<div class="home-road-arrow">↓</div>')
    st.markdown(
        f'<div class="home-roadmap-preview">{"".join(steps_html)}</div>',
        unsafe_allow_html=True,
    )

    if st.button("🗺️ View Complete Roadmap", type="primary", use_container_width=True, key="home_full_roadmap"):
        navigate_to(st.session_state, "roadmap")
        st.rerun()

    if st.button("📚 View Full Syllabus", use_container_width=True, key="home_cta_syllabus_after_roadmap"):
        navigate_to(st.session_state, "syllabus")
        st.rerun()


def _render_syllabus_preview() -> None:
    _section_anchor("home-syllabus", "Decision Section", "📚 Complete Syllabus Overview")
    st.caption("Major modules covered in the Master Class. Open the full syllabus for topics.")

    for i in range(0, len(HOME_SYLLABUS_PREVIEW), 2):
        cols = st.columns(2)
        for col, item in zip(cols, HOME_SYLLABUS_PREVIEW[i : i + 2]):
            with col:
                st.markdown(
                    f"""
                    <div class="ala-card syllabus-preview-card">
                      <div class="card-icon">{item['icon']}</div>
                      <div class="card-title">{item['title']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    if st.button("📚 Explore Full Syllabus", type="primary", use_container_width=True, key="home_full_syllabus"):
        navigate_to(st.session_state, "syllabus")
        st.rerun()

    if st.button("🚀 Join Now", use_container_width=True, key="home_join_after_syllabus"):
        navigate_to(st.session_state, "enquiry")
        st.rerun()


def render() -> None:
    _handle_quick_nav()
    render_page_header("home")
    render_hero()
    render_mobile_quick_nav()

    st.markdown("---")
    _render_roadmap_preview()

    st.markdown("---")
    _render_syllabus_preview()

    st.markdown("---")
    _section_anchor("home-highlights", "Program", "Course Highlights")
    render_cards(COURSE["highlights"], columns=3)

    st.markdown("---")
    _section_anchor("home-why", "Program", "Why This Program")
    render_cards(HOME_WHY, columns=3)
    st.markdown(
        '<div class="section-label" style="margin-top:1rem;">Market Context</div>',
        unsafe_allow_html=True,
    )
    render_cards(
        [{"icon": "📌", "title": m["title"], "body": m["body"]} for m in COURSE["market_context"]],
        columns=3,
    )

    st.markdown("---")
    _section_anchor("home-live", "Learn", "Live Classes")
    st.markdown(
        """
        <div class="live-pill-row">
          <div class="live-pill"><span class="live-dot"></span> LIVE</div>
          <div class="live-pill"><span class="live-dot"></span> INSTRUCTOR LED</div>
          <div class="live-pill"><span class="live-dot"></span> INTERACTIVE</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_cards(HOME_LIVE, columns=3)

    st.markdown("---")
    _section_anchor("home-interview", "Career", "Interview Preparation")
    render_cards(HOME_INTERVIEW, columns=3)
    st.markdown("##### 💬 WhatsApp Now")
    render_whatsapp_buttons("💬 WhatsApp")
    st.caption(
        f"Direct contact: {WHATSAPP_CONTACTS[0]['number']} · {WHATSAPP_CONTACTS[1]['number']}"
    )

    st.markdown("---")
    _section_anchor("home-tools", "Setup", "Tools & Applications")
    render_cards(HOME_TOOLS, columns=2)
    if st.button("🛠️ View All Tools", use_container_width=True, key="home_tools_btn"):
        navigate_to(st.session_state, "tools")
        st.rerun()

    st.markdown("---")
    _section_anchor("home-support", "Support", "Support")
    render_cards(HOME_SUPPORT, columns=3)

    st.markdown("---")
    _section_anchor("home-join", "Next Step", "Join Now")
    st.write("Start your Azure Data Engineering journey with live learning and a clear 90-day path.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button(
            "🚀 Join Now / Enquire",
            type="primary",
            use_container_width=True,
            key="home_final_join",
        ):
            navigate_to(st.session_state, "enquiry")
            st.rerun()
    with c2:
        st.link_button("💬 WhatsApp 1", WHATSAPP_CONTACTS[0]["url"], use_container_width=True)
