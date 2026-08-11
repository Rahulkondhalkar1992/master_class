"""
Azure Learnings Academy
Azure Data Engineering Master Class — Streamlit Course Portal (Phase 1)
"""

import streamlit as st

from components.navbar import render_footer, render_sidebar
from components.styles import inject_styles
from utils.navigation import init_navigation_state
from views import (
    ai_assistant,
    assignments,
    course_info,
    enquiry,
    home,
    learning_plan,
    project,
    python_practice,
    roadmap,
    sql_practice,
    syllabus,
    tools,
)

st.set_page_config(
    page_title="Azure Learnings Academy | Azure Data Engineering Master Class",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_styles()
init_navigation_state(st.session_state)
render_sidebar()

PAGE_RENDERERS = {
    "home": home.render,
    "course_info": course_info.render,
    "roadmap": roadmap.render,
    "learning_plan": learning_plan.render,
    "syllabus": syllabus.render,
    "tools": tools.render,
    "enquiry": enquiry.render,
    "project": project.render,
    "assignments": assignments.render,
    "sql_practice": sql_practice.render,
    "python_practice": python_practice.render,
    "ai_assistant": ai_assistant.render,
}

renderer = PAGE_RENDERERS.get(st.session_state.current_page, home.render)
renderer()
render_footer()
