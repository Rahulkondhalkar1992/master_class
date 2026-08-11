"""Roadmap visual component."""

import streamlit as st

from content.roadmap import ROADMAP


def render_roadmap() -> None:
    st.caption("Practical sequence — starts with ADF (not Python/SQL first).")
    for idx, step in enumerate(ROADMAP):
        badge = ""
        if step.get("coming_soon"):
            badge = (
                '<span class="exp-badge" style="background:rgba(139,92,246,0.22);color:#c4b5fd;">'
                "COMING SOON</span>"
            )
        st.markdown(
            f"""
            <div class="roadmap-step">
              <div class="roadmap-num">{step['id']}</div>
              <div style="flex:1;">
                <div style="font-size:1.05rem;font-weight:650;">
                  {step['icon']} {step['title']} {badge}
                </div>
                <div style="color:#94A3B8;font-size:0.92rem;margin-top:0.25rem;">
                  {step['desc']}
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if idx < len(ROADMAP) - 1:
            st.markdown('<div class="roadmap-connector">↓</div>', unsafe_allow_html=True)
