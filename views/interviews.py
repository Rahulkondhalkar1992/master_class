"""Interview preparation page."""

import streamlit as st

from components.cards import render_cards
from components.navbar import render_cta_row, render_page_header
from content.interviews import EXPERIENCE_TRACKS, MOCK_FOCUS, SAMPLE_QUESTIONS, SCENARIOS


def render() -> None:
    render_page_header("interviews")

    st.markdown('<div class="section-label">Experience Tracks</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for col, track in zip(cols, EXPERIENCE_TRACKS):
        with col:
            points = "".join(f"<li>{p}</li>" for p in track["points"])
            st.markdown(
                f"""
                <div class="ala-card">
                  <div class="exp-badge badge-years">{track['years']}</div>
                  <div class="card-title">{track['focus']}</div>
                  <ul style="color:#94A3B8;font-size:0.9rem;padding-left:1.1rem;margin:0.4rem 0 0;">
                    {points}
                  </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("Scenario-Based Preparation")
    render_cards(
        [{"icon": "🧩", "title": scenario, "body": "Discuss root cause, impact, and recovery approach."} for scenario in SCENARIOS],
        columns=2,
    )

    st.markdown("---")
    st.subheader("Sample Interview Questions")
    st.caption("Expandable preview — fuller question banks can be added per module later.")
    for q in SAMPLE_QUESTIONS:
        st.markdown(
            f"""
            <div class="question-card">
              <div class="q-num">{q['id']} · {q['module']}</div>
              <div style="font-weight:600;">{q['question']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.expander("▶ View Answer"):
            st.write(q["answer"])

    st.markdown("---")
    st.subheader("Mock Interview Focus")
    render_cards(
        [{"icon": "🎤", "title": m["title"], "body": m["body"]} for m in MOCK_FOCUS],
        columns=3,
    )
    render_cta_row(show_join=True, show_explore=False, show_contact=True)
