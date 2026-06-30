from langgraph.graph import StateGraph, START, END

from state import CareerState

from agents.profile_agent import profile_agent
from agents.search_agent import search_agent
from agents.matching_agent import matching_agent
from agents.cover_letter_agent import cover_letter_agent


def build_graph():
    """
    Builds and compiles the Career Agent workflow.
    """

    workflow = StateGraph(CareerState)

    # Add Nodes
    workflow.add_node("profile", profile_agent)
    workflow.add_node("search", search_agent)
    workflow.add_node("matching", matching_agent)
    workflow.add_node("cover_letter", cover_letter_agent)

    # Connect Nodes
    workflow.add_edge(START, "profile")
    workflow.add_edge("profile", "search")
    workflow.add_edge("search", "matching")
    workflow.add_edge("matching", "cover_letter")
    workflow.add_edge("cover_letter", END)

    return workflow.compile()