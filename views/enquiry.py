"""Enquiry / Join Now page."""

import streamlit as st

from components.navbar import render_page_header, render_whatsapp_buttons
from utils.validators import validate_email, validate_mobile, validate_name


def render() -> None:
    render_page_header("enquiry")
    st.subheader("Start Your Azure Data Engineering Journey")

    if st.session_state.get("enquiry_submitted"):
        st.success("✓ Thank you for your interest!")
        st.write("Our team will connect with you.")
        st.write("You can also contact us directly on WhatsApp.")
        render_whatsapp_buttons()
        if st.button("Submit another enquiry"):
            st.session_state.enquiry_submitted = False
            st.rerun()
        return

    with st.form("enquiry_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            full_name = st.text_input("Full Name *")
            mobile = st.text_input("Mobile Number *")
            email = st.text_input("Email")
            experience = st.selectbox(
                "Total Experience",
                [
                    "",
                    "Fresher / < 1 year",
                    "1–3 years",
                    "4–7 years",
                    "8–11 years",
                    "12+ years",
                ],
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

        # Phase 1: no database. Payload is ready for future storage/email/sheet integration.
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

    st.markdown("---")
    st.subheader("Prefer WhatsApp?")
    render_whatsapp_buttons()
