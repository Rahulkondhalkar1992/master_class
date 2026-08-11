"""Roadmap page."""

from components.navbar import render_cta_row, render_page_header
from components.roadmap import render_roadmap


def render() -> None:
    render_page_header("roadmap")
    render_roadmap()
    render_cta_row(show_join=True, show_explore=True, show_contact=True, explore_target="learning_plan")
