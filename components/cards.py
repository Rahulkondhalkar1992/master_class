"""Card and section helpers."""

import streamlit as st


def render_cards(items: list[dict], columns: int = 3) -> None:
    for i in range(0, len(items), columns):
        cols = st.columns(columns)
        for col, item in zip(cols, items[i : i + columns]):
            with col:
                st.markdown(
                    f"""
                    <div class="ala-card">
                      <div class="card-icon">{item.get('icon', '')}</div>
                      <div class="card-title">{item.get('title', '')}</div>
                      <p class="card-body">{item.get('body', '')}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def render_feature_rows(items: list[dict]) -> None:
    for item in items:
        st.markdown(
            f"""
            <div class="feature-row">
              <div class="fr-icon">{item.get('icon', '')}</div>
              <div>
                <div class="fr-title">{item.get('title', '')}</div>
                <p class="fr-body">{item.get('body', '')}</p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_flow(nodes: list[str]) -> None:
    parts = []
    for idx, node in enumerate(nodes):
        parts.append(f'<span class="flow-node">{node}</span>')
        if idx < len(nodes) - 1:
            parts.append('<span class="flow-arrow">→</span>')
    st.markdown(f'<div class="flow-rail">{"".join(parts)}</div>', unsafe_allow_html=True)


def render_coming_soon(
    icon: str,
    title: str,
    body: str,
    chips: list[str] | None = None,
    status: str = "Coming Soon",
) -> None:
    chips_html = "".join(f'<span class="cs-chip">{chip}</span>' for chip in (chips or []))
    st.markdown(
        f"""
        <div class="coming-soon-box">
          <div class="cs-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{body}</p>
          <div style="margin:0.8rem 0 0.35rem;font-weight:650;color:#c4b5fd;letter-spacing:0.08em;">
            {status.upper()}
          </div>
          <div style="color:#94A3B8;font-size:0.9rem;margin-bottom:1rem;">
            Work in Progress · Available in upcoming releases
          </div>
          <div>{chips_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_wip_page(
    icon: str,
    title: str,
    body: str,
    features: list[dict] | None = None,
    chips: list[str] | None = None,
) -> None:
    render_coming_soon(icon=icon, title=title, body=body, chips=chips, status="Coming Soon")
    if features:
        st.markdown("---")
        st.subheader("Planned experience")
        render_cards(features, columns=3)
