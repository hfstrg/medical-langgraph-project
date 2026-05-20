from langgraph.graph import StateGraph, END

from app.state import MedicalState

from app.nodes.supervisor import supervisor
from app.nodes.diagnostic_agent import diagnostic_agent
from app.nodes.physician_review import physician_review
from app.nodes.report_agent import report_agent


def route_next(state: MedicalState):

    return state.get("next", "FINISH")


def create_graph():

    workflow = StateGraph(MedicalState)

    workflow.add_node("supervisor", supervisor)
    workflow.add_node("diagnostic_agent", diagnostic_agent)
    workflow.add_node("physician_review", physician_review)
    workflow.add_node("report_agent", report_agent)

    workflow.set_entry_point("supervisor")

    workflow.add_conditional_edges(
        "supervisor",
        route_next,
        {
            "diagnostic_agent": "diagnostic_agent",
            "physician_review": "physician_review",
            "report_agent": "report_agent",
            "FINISH": END
        }
    )

    workflow.add_edge("diagnostic_agent", "supervisor")
    workflow.add_edge("physician_review", "supervisor")
    workflow.add_edge("report_agent", "supervisor")

    return workflow.compile()