"""Shared page chrome components."""

import streamlit as st

from utils.navigation import NAV_SECTIONS, PAGE_META, navigate_to
from utils.whatsapp import WHATSAPP_CONTACTS


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
              <div class="brand-top">Azure Learnings</div>
              <div class="brand-name">ACADEMY</div>
              <div class="brand-sub">Azure Data Engineering Master Class</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        current = st.session_state.current_page
        for section in NAV_SECTIONS:
            if section["label"]:
                st.markdown(
                    f'<div class="nav-section-label">{section["label"]}</div>',
                    unsafe_allow_html=True,
                )
            for item in section["items"]:
                label = f'{item["icon"]}  {item["label"]}'
                is_active = current == item["key"]
                if st.button(
                    label,
                    key=f"nav_{item['key']}",
                    use_container_width=True,
                    type="primary" if is_active else "secondary",
                ):
                    navigate_to(
                        st.session_state,
                        item["key"],
                        syllabus_key=item.get("syllabus_key"),
                    )
                    st.rerun()
                if item.get("badge"):
                    st.caption(f"  {item['badge']}")


def render_page_header(page_key: str, override: dict | None = None) -> None:
    meta = override or PAGE_META.get(page_key, {})
    st.markdown(
        f"""
        <div class="page-header">
          <div class="page-icon">{meta.get('icon', '')}</div>
          <h1>{meta.get('title', '')}</h1>
          <p>{meta.get('description', '')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    contacts = " · ".join(
        f'<a href="{c["url"]}" target="_blank">{c["number"]}</a>' for c in WHATSAPP_CONTACTS
    )
    st.markdown(
        f"""
        <div class="footer-bar">
          <div class="footer-brand">Azure Learnings ACADEMY</div>
          <div>Azure Data Engineering Master Class</div>
          <div style="margin:0.45rem 0;">Learn • Practice • Build • Prepare</div>
          <div>WhatsApp: {contacts}</div>
          <div style="margin-top:0.6rem;">© 2026 Azure Learnings Academy</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_whatsapp_buttons(label_prefix: str = "💬 WhatsApp") -> None:
    cols = st.columns(2)
    for idx, contact in enumerate(WHATSAPP_CONTACTS):
        with cols[idx]:
            st.link_button(
                f'{label_prefix}: {contact["number"]}',
                contact["url"],
                use_container_width=True,
            )


def render_cta_row(
    *,
    show_join: bool = True,
    show_explore: bool = False,
    show_contact: bool = True,
    explore_target: str = "course_info",
) -> None:
    buttons = []
    if show_join:
        buttons.append(("join", "🚀 Join Now", "enquiry"))
    if show_explore:
        buttons.append(("explore", "📚 Explore Course", explore_target))
    if show_contact:
        buttons.append(("contact", "💬 Contact Now", None))

    cols = st.columns(len(buttons) or 1)
    for col, (key, label, target) in zip(cols, buttons):
        with col:
            if target:
                if st.button(
                    label,
                    key=f"cta_{key}_{target}",
                    use_container_width=True,
                    type="primary" if key == "join" else "secondary",
                ):
                    navigate_to(st.session_state, target)
                    st.rerun()
            else:
                st.link_button(label, WHATSAPP_CONTACTS[0]["url"], use_container_width=True)
