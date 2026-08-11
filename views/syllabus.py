"""Syllabus page — all modules on main screen, collapsed by default."""

import streamlit as st

from components.navbar import render_cta_row, render_page_header
from components.syllabus import render_syllabus


def render(module_key: str | None = None) -> None:
    render_page_header("syllabus")
    focus = module_key or st.session_state.get("syllabus_focus")
    # Clear one-shot focus after using so revisit stays collapsed
    if focus and st.session_state.get("syllabus_focus") == focus:
        st.session_state.syllabus_focus = None
    render_syllabus(focus_key=focus)
    render_cta_row(show_join=True, show_explore=False, show_contact=True)
