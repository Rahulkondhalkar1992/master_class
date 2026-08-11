"""Support page."""

import streamlit as st

from components.cards import render_cards
from components.navbar import render_cta_row, render_page_header, render_whatsapp_buttons
from content.support import SUPPORT


def render() -> None:
    render_page_header("support")

    st.markdown(
        f"""
        <div style="text-align:center;margin:0.5rem 0 1.4rem;">
          <div class="support-hero-num">{SUPPORT['headline']}</div>
          <div style="letter-spacing:0.16em;font-weight:700;margin-top:0.35rem;">
            {SUPPORT['subheadline']}
          </div>
          <p style="color:#94A3B8;max-width:640px;margin:0.8rem auto 0;">{SUPPORT['intro']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_cards(
        [{"icon": a["icon"], "title": a["title"], "body": a["body"]} for a in SUPPORT["areas"]],
        columns=3,
    )

    st.markdown("---")
    st.subheader("Need help right away?")
    render_whatsapp_buttons()
    render_cta_row(show_join=True, show_explore=False, show_contact=False)
