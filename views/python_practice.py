"""Coming Soon — Python Practice."""

from components.cards import render_wip_page
from components.navbar import render_cta_row, render_page_header


def render() -> None:
    render_page_header("python_practice")
    render_wip_page(
        icon="🐍",
        title="Python Practice Lab",
        body=(
            "A secure Python practice sandbox is being prepared. "
            "Arbitrary code execution is intentionally disabled until the engine is ready."
        ),
        chips=["Lists", "Dictionaries", "Functions", "JSON", "Transforms"],
        features=[
            {"icon": "🧩", "title": "Challenges", "body": "Data-engineering oriented Python exercises."},
            {"icon": "🔒", "title": "Safe runtime", "body": "Controlled execution — no unsafe eval/exec."},
            {"icon": "🧠", "title": "Interview ready", "body": "Patterns commonly asked in DE interviews."},
        ],
    )
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="syllabus")
