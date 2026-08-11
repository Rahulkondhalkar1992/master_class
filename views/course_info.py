"""Course information page with required subsections."""

import streamlit as st

from components.cards import render_flow
from components.navbar import render_cta_row, render_page_header
from content.course import COURSE, COURSE_INFO_SECTIONS, LEARNING_PLAN_90
from utils.navigation import navigate_to


def render() -> None:
    render_page_header("course_info")

    tabs = st.tabs([f"{s['icon']} {s['title']}" for s in COURSE_INFO_SECTIONS] + ["🗺️ 90-Day Roadmap"])

    for tab, section in zip(tabs[:-1], COURSE_INFO_SECTIONS):
        with tab:
            st.subheader(f"{section['icon']} {section['title']}")
            if section.get("body"):
                st.write(section["body"])
            if section.get("flow"):
                render_flow(section["flow"])
            if section.get("items"):
                for item in section["items"]:
                    st.markdown(f"- {item}")
            if section.get("note"):
                st.info(section["note"])
            if section["key"] == "about":
                st.write(COURSE["objective"])

    with tabs[-1]:
        st.subheader("🗺️ 90-Day Roadmap")
        st.write("Structured 3-month learning plan overview. Open the full plan for details.")
        for block in LEARNING_PLAN_90:
            st.markdown(f"**{block['days']} — {block['title']}**")
            for focus in block["focus"]:
                st.markdown(f"- {focus}")
        if st.button("Open 3 Months Learning Plan", type="primary"):
            navigate_to(st.session_state, "learning_plan")
            st.rerun()

    st.markdown("---")
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="roadmap")
