"""Coming Soon — Real-Time Project."""

from components.cards import render_wip_page
from components.navbar import render_cta_row, render_page_header


def render() -> None:
    render_page_header("project")
    render_wip_page(
        icon="🏗️",
        title="Real-Time Industry Project",
        body=(
            "The end-to-end Azure data engineering project experience is being prepared. "
            "You will build from business requirement through ingestion, lakehouse layers, "
            "quality, monitoring, and final architecture."
        ),
        chips=["ADF", "ADLS", "Databricks", "Delta", "Medallion", "CI/CD"],
        features=[
            {"icon": "📋", "title": "Business first", "body": "Requirement-driven architecture and delivery."},
            {"icon": "🔁", "title": "End-to-end", "body": "Source → ADF → Lake → Transform → Model → Monitor."},
            {"icon": "🛠️", "title": "Implementation", "body": "Hands-on build across core Azure data services."},
        ],
    )
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="roadmap")
