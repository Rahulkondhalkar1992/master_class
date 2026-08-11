"""3 Months / 90-day learning plan page."""

import streamlit as st

from components.navbar import render_cta_row, render_page_header
from content.course import LEARNING_PLAN_90
from content.syllabus import get_module_by_key
from utils.navigation import navigate_to


def render() -> None:
    render_page_header("learning_plan")

    for block in LEARNING_PLAN_90:
        st.markdown(
            f"""
            <div class="roadmap-step">
              <div class="roadmap-num">{block['icon']}</div>
              <div>
                <div style="color:#22D3EE;font-size:0.8rem;letter-spacing:0.08em;font-weight:650;">
                  {block['days']}
                </div>
                <div style="font-size:1.15rem;font-weight:700;margin-top:0.2rem;">
                  {block['title']}
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for focus in block["focus"]:
            st.markdown(f"- {focus}")

        related = []
        for mod_key in block["modules"]:
            module = get_module_by_key(mod_key)
            if module:
                related.append(f"{module['number']} {module['title']}")
        if related:
            st.caption("Related syllabus: " + " · ".join(related))

        st.markdown("---")

    if st.button("📚 Open Full Syllabus", type="primary"):
        navigate_to(st.session_state, "syllabus")
        st.rerun()

    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="roadmap")
