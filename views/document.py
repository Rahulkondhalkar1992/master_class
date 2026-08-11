"""
Classic single-page study material / document viewer.
All learning content lives below the hero — no sidebar, no separate Roadmap page.
"""

import streamlit as st

from components.cards import render_cards
from components.hero import (
    render_hero,
    render_instructors,
    render_mobile_dock,
    render_program_banner,
    render_toc,
)
from components.navbar import render_same_window_link, render_whatsapp_buttons
from components.syllabus import render_syllabus
from content.coming_soon import COMING_SOON_ITEMS
from content.course import COURSE, COURSE_INFO_SECTIONS, LEARNING_PLAN_90
from content.home import HOME_INTERVIEW, HOME_LIVE, HOME_SUPPORT, HOME_WHY
from content.support import SUPPORT
from content.syllabus import get_module_by_key
from content.tools import TOOL_CATEGORIES
from utils.validators import validate_email, validate_mobile, validate_name
from utils.whatsapp import WHATSAPP_CONTACTS


def _chapter(num: str, anchor: str, title: str, subtitle: str = "") -> None:
    sub = f'<p class="chapter-sub">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <section id="{anchor}" class="doc-chapter">
          <div class="chapter-meta">
            <span class="chapter-num">Chapter {num}</span>
            <a class="chapter-top" href="#top" target="_self">↑ Top</a>
          </div>
          <h2 class="chapter-title">{title}</h2>
          {sub}
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_course_info() -> None:
    _chapter(
        "01",
        "sec-info",
        "Course Information",
        "Welcome, objectives, prerequisites, setup, and how to use this study portal.",
    )
    for section in COURSE_INFO_SECTIONS:
        with st.expander(f"{section['icon']}  {section['title']}", expanded=False):
            if section.get("body"):
                st.write(section["body"])
            if section.get("flow"):
                st.markdown(
                    '<div class="doc-flow">'
                    + " → ".join(f'<span class="doc-flow-node">{s}</span>' for s in section["flow"])
                    + "</div>",
                    unsafe_allow_html=True,
                )
            if section.get("items"):
                for item in section["items"]:
                    st.markdown(f"- {item}")
            if section.get("note"):
                st.info(section["note"])
            if section["key"] == "about":
                st.write(COURSE["objective"])


def _render_learning_plan() -> None:
    _chapter(
        "02",
        "sec-plan",
        "3-Month Learning Plan",
        "Your structured 90-day journey — the single roadmap for this Master Class.",
    )
    st.markdown(
        """
        <div class="plan-intro">
          Start with Azure &amp; Storage, deepen through ADF, then SQL, modeling, Python,
          Databricks, Delta Lake, advanced topics, and the end-to-end project.
          <strong>This plan replaces a separate roadmap page</strong> — one clear learning path.
        </div>
        """,
        unsafe_allow_html=True,
    )
    for block in LEARNING_PLAN_90:
        with st.expander(f"{block['icon']}  {block['days']} — {block['title']}", expanded=False):
            for focus in block["focus"]:
                st.markdown(f"- {focus}")
            related = []
            for mod_key in block["modules"]:
                module = get_module_by_key(mod_key)
                if module:
                    related.append(f"{module['number']} {module['title']}")
            if related:
                st.caption("Syllabus modules: " + " · ".join(related))


def _render_syllabus() -> None:
    _chapter(
        "03",
        "sec-syllabus",
        "Complete Syllabus",
        "Expand any module to read topics. Designed like a classic curriculum document.",
    )
    st.caption("Modules start collapsed. Click a module title to expand study topics.")
    render_syllabus(focus_key=None)


def _render_highlights_and_why() -> None:
    _chapter("04", "sec-highlights", "Program Highlights", "Why learners choose this Master Class.")
    render_cards(COURSE["highlights"], columns=3)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### Why This Program")
    render_cards(HOME_WHY, columns=3)

    st.markdown("### Live Classroom Experience")
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
    render_cards(HOME_LIVE, columns=3)

    st.markdown("### Market Context")
    render_cards(
        [{"icon": "📌", "title": m["title"], "body": m["body"]} for m in COURSE["market_context"]],
        columns=3,
    )


def _render_interview() -> None:
    _chapter(
        "05",
        "sec-interview",
        "Interview Preparation",
        "Scenario, architecture, and mock-interview readiness.",
    )
    render_cards(HOME_INTERVIEW, columns=3)
    st.markdown("##### Contact on WhatsApp")
    render_whatsapp_buttons()


def _render_tools() -> None:
    _chapter(
        "06",
        "sec-tools",
        "Tools & Applications",
        "Setup references for the tools used throughout the course. Links open in the same window.",
    )
    for category in TOOL_CATEGORIES:
        st.markdown(f"#### {category['name']}")
        for tool in category["tools"]:
            with st.expander(f"🛠️  {tool['name']}", expanded=False):
                st.markdown(f"**Purpose:** {tool['purpose']}")
                st.markdown(f"**Why required:** {tool['why']}")
                st.markdown(f"**Course usage:** {tool['usage']}")
                render_same_window_link("Open official docs / setup →", tool["docs"])


def _render_coming_soon() -> None:
    _chapter(
        "07",
        "sec-coming",
        "Coming Soon · Work in Progress",
        "Upcoming learning experiences — clubbed in one place for clarity.",
    )
    st.markdown(
        """
        <div class="wip-banner">
          <span class="wip-pulse"></span>
          Available in upcoming releases · Premium practice &amp; project experiences in progress
        </div>
        """,
        unsafe_allow_html=True,
    )
    for item in COMING_SOON_ITEMS:
        tags = "".join(f'<span class="cs-chip">{t}</span>' for t in item["tags"])
        st.markdown(
            f"""
            <div class="wip-card">
              <div class="wip-card-top">
                <span class="wip-icon">{item['icon']}</span>
                <span class="wip-status">{item['status']}</span>
              </div>
              <div class="wip-title">{item['title']}</div>
              <p class="wip-body">{item['body']}</p>
              <div>{tags}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _render_support() -> None:
    st.markdown("### Support Framework")
    st.markdown(
        f"""
        <div class="support-strip">
          <div class="support-hero-num">{SUPPORT['headline']}</div>
          <div class="support-strip-copy">
            <div class="support-sub">{SUPPORT['subheadline']}</div>
            <p>{SUPPORT['intro']}</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_cards(HOME_SUPPORT, columns=3)


def _render_enquiry() -> None:
    _chapter(
        "08",
        "sec-join",
        "Join Now · Enquiry",
        "Share your details — our team will connect with you.",
    )

    if st.session_state.get("enquiry_submitted"):
        st.success("✓ Thank you for your interest! Our team will connect with you.")
        st.write("You can also contact us directly on WhatsApp (opens in the same window).")
        render_whatsapp_buttons()
        if st.button("Submit another enquiry", key="doc_enq_again"):
            st.session_state.enquiry_submitted = False
            st.rerun()
        return

    with st.form("doc_enquiry_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            full_name = st.text_input("Full Name *")
            mobile = st.text_input("Mobile Number *")
            email = st.text_input("Email")
            experience = st.selectbox(
                "Total Experience",
                ["", "Fresher / < 1 year", "1–3 years", "4–7 years", "8–11 years", "12+ years"],
            )
        with c2:
            company = st.text_input("Current Company")
            role = st.text_input("Current Role")
            skillset = st.text_input("Current Technology / Skillset")
            mode = st.selectbox(
                "Preferred Learning Mode",
                ["", "Weekday Live", "Weekend Live", "Need guidance"],
            )
        message = st.text_area("Message / Questions")
        submitted = st.form_submit_button("🚀 Submit Enquiry", use_container_width=True)

    if submitted:
        ok_name, name_msg = validate_name(full_name)
        ok_mobile, mobile_msg = validate_mobile(mobile)
        ok_email, email_msg = validate_email(email, required=False)
        errors = []
        if not ok_name:
            errors.append(name_msg)
        if not ok_mobile:
            errors.append(mobile_msg)
        if not ok_email:
            errors.append(email_msg)
        if errors:
            for err in errors:
                st.error(err)
            return
        st.session_state.last_enquiry = {
            "full_name": full_name.strip(),
            "mobile": mobile_msg,
            "email": email.strip(),
            "experience": experience,
            "company": company.strip(),
            "role": role.strip(),
            "skillset": skillset.strip(),
            "preferred_mode": mode,
            "message": message.strip(),
        }
        st.session_state.enquiry_submitted = True
        st.rerun()

    st.markdown("##### Prefer WhatsApp?")
    render_whatsapp_buttons()
    st.caption(
        f"Numbers: {WHATSAPP_CONTACTS[0]['number']} · {WHATSAPP_CONTACTS[1]['number']}"
    )


def render() -> None:
    render_hero()
    render_program_banner()
    render_toc()

    st.markdown('<div class="doc-paper">', unsafe_allow_html=True)

    _render_course_info()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_learning_plan()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_syllabus()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_highlights_and_why()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_interview()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_tools()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_coming_soon()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_support()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    render_instructors()
    st.markdown('<hr class="doc-rule" />', unsafe_allow_html=True)

    _render_enquiry()

    st.markdown("</div>", unsafe_allow_html=True)
    render_mobile_dock()
