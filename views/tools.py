"""Tools and applications page."""

import streamlit as st

from components.navbar import render_cta_row, render_page_header
from content.tools import TOOL_CATEGORIES


def render() -> None:
    render_page_header("tools")

    for category in TOOL_CATEGORIES:
        st.markdown(f'<div class="section-label">{category["name"]}</div>', unsafe_allow_html=True)
        st.subheader(category["name"])
        for i in range(0, len(category["tools"]), 3):
            cols = st.columns(3)
            for col, tool in zip(cols, category["tools"][i : i + 3]):
                with col:
                    st.markdown(
                        f"""
                        <div class="ala-card">
                          <div class="card-title">{tool['name']}</div>
                          <p class="card-body"><strong>Purpose:</strong> {tool['purpose']}</p>
                          <p class="card-body"><strong>Why required:</strong> {tool['why']}</p>
                          <p class="card-body"><strong>Course usage:</strong> {tool['usage']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.link_button("Open Docs / Setup", tool["docs"], use_container_width=True)
        st.markdown("---")

    render_cta_row(show_join=True, show_explore=False, show_contact=True)
