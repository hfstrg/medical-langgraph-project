from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.state import MedicalState
from app.tools.patient_tools import ask_patient
from app.tools.mcp_client import get_mcp_recommendation


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)


def diagnostic_agent(state: MedicalState):

    question_count = state.get("question_count", 0)

    if question_count < 5:

        question = ask_patient(question_count)

        return {
            "messages": [
                {
                    "role": "assistant",
                    "content": question
                }
            ],
            "question_count": question_count + 1
        }

    symptoms = state.get("symptoms", "")

    prompt = f"""
Tu es un assistant médical académique.

Patient :
{symptoms}

Produis :
1. Une synthèse clinique préliminaire
2. Une orientation prudente
3. Des risques possibles

Ne donne jamais un diagnostic définitif.
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    interim = get_mcp_recommendation(symptoms)

    return {
        "diagnostic_summary": response.content,
        "interim_care": interim,
        "next": "physician_review"
    }
