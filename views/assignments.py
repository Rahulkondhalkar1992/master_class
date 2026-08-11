"""Coming Soon — Assignments."""

from components.cards import render_wip_page
from components.navbar import render_cta_row, render_page_header


def render() -> None:
    render_page_header("assignments")
    render_wip_page(
        icon="📝",
        title="Assignments Hub",
        body=(
            "Assignment packs for Azure, ADF, SQL, Python, PySpark, Databricks, and the project "
            "are in progress and will be released in upcoming updates."
        ),
        chips=["Azure", "ADF", "SQL", "Python", "PySpark", "Databricks", "Project"],
        features=[
            {"icon": "🗄️", "title": "SQL Track", "body": "Beginner to advanced practical SQL problems."},
            {"icon": "🔄", "title": "ADF Track", "body": "Pipeline and framework-focused assignments."},
            {"icon": "🔥", "title": "Databricks Track", "body": "Notebook, job, and transformation challenges."},
        ],
    )
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="syllabus")
