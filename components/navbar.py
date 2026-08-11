"""Shared chrome — footer and same-window contact links (no sidebar)."""

import streamlit as st

from utils.whatsapp import WHATSAPP_CONTACTS


def render_same_window_link(label: str, url: str, *, primary: bool = False) -> None:
    cls = "doc-btn doc-btn-primary" if primary else "doc-btn"
    st.markdown(
        f'<a class="{cls}" href="{url}" target="_self" rel="noopener noreferrer">{label}</a>',
        unsafe_allow_html=True,
    )


def render_whatsapp_buttons(label_prefix: str = "💬 WhatsApp") -> None:
    cols = st.columns(2)
    for idx, contact in enumerate(WHATSAPP_CONTACTS):
        with cols[idx]:
            render_same_window_link(
                f'{label_prefix}: {contact["number"]}',
                contact["url"],
                primary=idx == 0,
            )


def render_footer() -> None:
    contacts = " · ".join(
        f'<a href="{c["url"]}" target="_self" rel="noopener noreferrer">{c["number"]}</a>'
        for c in WHATSAPP_CONTACTS
    )
    st.markdown(
        f"""
        <footer class="doc-footer">
          <div class="doc-footer-brand">Azure Learnings ACADEMY</div>
          <div>Azure Data Engineering Master Class</div>
          <div class="doc-footer-tag">Learn · Practice · Build · Prepare</div>
          <div>WhatsApp: {contacts}</div>
          <div class="doc-footer-copy">© 2026 Azure Learnings Academy</div>
        </footer>
        """,
        unsafe_allow_html=True,
    )
