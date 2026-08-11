"""Why this program page."""

import streamlit as st

from components.cards import render_cards, render_feature_rows
from components.navbar import render_cta_row, render_page_header
from content.course import COURSE


def render() -> None:
    render_page_header("why_program")
    render_feature_rows(COURSE["why_points"])

    st.markdown("---")
    st.subheader("📈 Why Azure Data Engineering?")
    render_cards(
        [{"icon": "📌", "title": m["title"], "body": m["body"]} for m in COURSE["market_context"]],
        columns=3,
    )
    st.caption("No invented salary, placement, or demand statistics are shown.")

    st.markdown("---")
    render_cta_row(show_join=True, show_explore=True, show_contact=True)
