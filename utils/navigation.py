"""Sidebar navigation configuration and helpers."""

NAV_SECTIONS = [
    {
        "label": None,
        "items": [
            {"key": "home", "label": "Home", "icon": "🏠"},
        ],
    },
    {
        "label": "DISCOVER",
        "items": [
            {"key": "course_info", "label": "Course Information", "icon": "📢"},
            {"key": "roadmap", "label": "Roadmap", "icon": "🗺️"},
            {"key": "learning_plan", "label": "3 Months Learning Plan", "icon": "🗓️"},
            {"key": "syllabus", "label": "Syllabus", "icon": "📚"},
        ],
    },
    {
        "label": "COMING SOON",
        "items": [
            {"key": "project", "label": "Real-Time Project", "icon": "🏗️", "badge": "Work in Progress"},
            {"key": "assignments", "label": "Assignments", "icon": "📝", "badge": "Coming Soon"},
            {"key": "sql_practice", "label": "SQL Practice", "icon": "🗄️", "badge": "Coming Soon"},
            {"key": "python_practice", "label": "Python Practice", "icon": "🐍", "badge": "Coming Soon"},
            {"key": "ai_assistant", "label": "AI Assistant Program", "icon": "🤖", "badge": "Coming Soon"},
        ],
    },
    {
        "label": "SUPPORT",
        "items": [
            {"key": "tools", "label": "Tools & Applications", "icon": "🛠️"},
            {"key": "enquiry", "label": "Enquiry / Join Now", "icon": "📩"},
        ],
    },
]


PAGE_META = {
    "home": {
        "title": "Azure Data Engineering Master Class",
        "icon": "☁️",
        "description": "Become industry-ready through live learning, real projects, and interview preparation.",
    },
    "course_info": {
        "title": "Course Information",
        "icon": "📢",
        "description": "Welcome, about the course, prerequisites, tools setup, Azure account, and learning methodology.",
    },
    "roadmap": {
        "title": "Learning Roadmap",
        "icon": "🗺️",
        "description": "ADF-first practical journey — pipelines, Databricks, SQL, modeling, Python, advanced topics, and project.",
    },
    "learning_plan": {
        "title": "3 Months Learning Plan",
        "icon": "🗓️",
        "description": "A structured 90-day plan from Azure & Storage through the end-to-end project.",
    },
    "syllabus": {
        "title": "Complete Syllabus",
        "icon": "📚",
        "description": "Click a module to expand topics and details. All modules start collapsed.",
    },
    "project": {
        "title": "Real-Time Project",
        "icon": "🏗️",
        "description": "End-to-end industry project experience — available in an upcoming release.",
    },
    "assignments": {
        "title": "Assignments",
        "icon": "📝",
        "description": "Practical assignment packs — coming soon.",
    },
    "tools": {
        "title": "Tools & Applications",
        "icon": "🛠️",
        "description": "Setup the tools you will use throughout the Azure Data Engineering journey.",
    },
    "sql_practice": {
        "title": "SQL Practice",
        "icon": "🗄️",
        "description": "Interactive SQL practice lab — coming soon.",
    },
    "python_practice": {
        "title": "Python Practice",
        "icon": "🐍",
        "description": "Interactive Python practice lab — coming soon.",
    },
    "ai_assistant": {
        "title": "AI Assistant Program",
        "icon": "🤖",
        "description": "Your personal Azure Data Engineering mentor — coming soon.",
    },
    "enquiry": {
        "title": "Enquiry / Join Now",
        "icon": "📩",
        "description": "Share your details and our team will connect with you.",
    },
}


def init_navigation_state(session_state) -> None:
    if "current_page" not in session_state:
        session_state.current_page = "home"
    if "syllabus_focus" not in session_state:
        session_state.syllabus_focus = None


def navigate_to(session_state, page_key: str, syllabus_key: str | None = None) -> None:
    session_state.current_page = page_key
    if syllabus_key is not None:
        session_state.syllabus_focus = syllabus_key
