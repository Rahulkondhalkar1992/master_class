"""Coming Soon — SQL Practice."""

from components.cards import render_wip_page
from components.navbar import render_cta_row, render_page_header


def render() -> None:
    render_page_header("sql_practice")
    render_wip_page(
        icon="🗄️",
        title="SQL Practice Lab",
        body=(
            "An interactive SQL practice engine is under development. "
            "You will write queries, run them securely, and solve data engineering scenarios."
        ),
        chips=["Joins", "CTEs", "Window Functions", "Business Scenarios"],
        features=[
            {"icon": "❓", "title": "Question bank", "body": "Curated SQL challenges for data engineers."},
            {"icon": "▶️", "title": "Run queries", "body": "SQLite-compatible execution planned next."},
            {"icon": "📈", "title": "Progress", "body": "Practice tracking will arrive in a later release."},
        ],
    )
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="syllabus")
