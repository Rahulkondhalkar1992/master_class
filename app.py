"""
Azure Learnings Academy — Document Portal
Single-page classic study material / document viewer.
"""

import streamlit as st

from components.navbar import render_footer
from components.styles import inject_styles
from views import document

st.set_page_config(
    page_title="Azure Learnings Academy | Azure Data Engineering Master Class",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_styles()
document.render()
render_footer()
