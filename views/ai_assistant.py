"""Coming Soon — AI Assistant Program."""

from components.cards import render_wip_page
from components.navbar import render_cta_row, render_page_header


def render() -> None:
    render_page_header("ai_assistant")
    render_wip_page(
        icon="🤖",
        title="Azure Learnings AI Assistant Program",
        body=(
            "Your personal Azure Data Engineering mentor is being prepared. "
            "Ask about Azure, ADF, Databricks, PySpark, SQL, Python, and interview prep — soon."
        ),
        chips=["Azure", "ADF", "Databricks", "PySpark", "SQL", "Python", "Interviews"],
        features=[
            {"icon": "💬", "title": "Ask concepts", "body": "Clarify architecture and service questions."},
            {"icon": "🎯", "title": "Interview coach", "body": "Practice framing technical answers."},
            {"icon": "📚", "title": "Module aligned", "body": "Guidance mapped to the course syllabus."},
        ],
    )
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="roadmap")
