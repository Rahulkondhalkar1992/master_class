"""Syllabus expandable UI with nested topics."""

import streamlit as st

from content.syllabus import SYLLABUS, count_topics


def _star_label(title: str, star: bool = False, stars: int = 1) -> str:
    if not star and stars <= 1:
        return title
    mark = "⭐" * max(stars, 1)
    return f"{title} {mark}"


def _render_topic_tree(topics: list, depth: int = 0) -> None:
    for topic in topics:
        if isinstance(topic, str):
            indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * depth
            st.markdown(f"{indent}- {topic}", unsafe_allow_html=True)
            continue

        title = _star_label(
            topic.get("title", ""),
            star=bool(topic.get("star")),
            stars=int(topic.get("stars", 1 if topic.get("star") else 0)),
        )
        children = topic.get("children") or []
        if children:
            with st.expander(("  " * depth) + f"▸ {title}", expanded=False):
                for child in children:
                    if isinstance(child, str):
                        st.markdown(f"- {child}")
                    elif isinstance(child, dict):
                        _render_topic_tree([child], depth=0)
        else:
            indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * depth
            st.markdown(f"{indent}- {title}", unsafe_allow_html=True)


def render_module_detail(module: dict, expanded: bool = False) -> None:
    label = f"{module['number']}  {module['icon']}  {module['title']}"
    with st.expander(label, expanded=expanded):
        st.markdown(f"**{module['description']}**")
        st.caption(f"{count_topics(module['topics'])} topics in this module")
        st.markdown("#### Topics")
        _render_topic_tree(module["topics"])


def render_syllabus(focus_key: str | None = None) -> None:
    """Render all modules. Only a focused module (if any) starts expanded."""
    for module in SYLLABUS:
        render_module_detail(module, expanded=(focus_key is not None and module["key"] == focus_key))
