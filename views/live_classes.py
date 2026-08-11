"""Live classes page."""

import streamlit as st

from components.cards import render_cards
from components.navbar import render_cta_row, render_page_header
from content.support import LIVE_FLOW


def render() -> None:
    render_page_header("live_classes")

    st.markdown(
        """
        <div class="live-pill-row">
          <div class="live-pill"><span class="live-dot"></span> LIVE</div>
          <div class="live-pill"><span class="live-dot"></span> INSTRUCTOR LED</div>
          <div class="live-pill"><span class="live-dot"></span> INTERACTIVE</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("No Recorded-Only Learning")
    st.write(
        "Sessions are designed around live instruction, demos, coding, questions, "
        "and hands-on practice so concepts are reinforced in real time."
    )

    st.markdown('<div class="section-label">Classroom Flow</div>', unsafe_allow_html=True)
    parts = []
    for idx, step in enumerate(LIVE_FLOW):
        parts.append(
            f'<span class="flow-node">{step["icon"]} {step["title"]}</span>'
        )
        if idx < len(LIVE_FLOW) - 1:
            parts.append('<span class="flow-arrow">↓</span>')
    st.markdown(f'<div class="flow-rail">{"".join(parts)}</div>', unsafe_allow_html=True)

    render_cards(
        [
            {
                "icon": "👨‍🏫",
                "title": "Instructor-led",
                "body": "Guided sessions with structured explanations and live demos.",
            },
            {
                "icon": "💻",
                "title": "Real-time coding",
                "body": "Watch concepts being implemented, not only described.",
            },
            {
                "icon": "🙋",
                "title": "Student questions",
                "body": "Ask doubts during the session and clarify immediately.",
            },
            {
                "icon": "🧪",
                "title": "Hands-on exercises",
                "body": "Practice while the learning is still fresh.",
            },
            {
                "icon": "🏗️",
                "title": "Project discussion",
                "body": "Connect classroom topics to the real-time project.",
            },
            {
                "icon": "💬",
                "title": "Doubt resolution",
                "body": "Close gaps before moving to the next module.",
            },
        ],
        columns=3,
    )

    st.info("Class schedule and timing will appear here once configured. No invented timetable is shown.")
    render_cta_row(show_join=True, show_explore=False, show_contact=True)
