from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.state import MedicalState


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)


def report_agent(state: MedicalState):

    prompt = f"""
Génère un rapport clinique structuré.

Symptômes :
{state.get("symptoms")}

Synthèse clinique :
{state.get("diagnostic_summary")}

Recommandation intermédiaire :
{state.get("interim_care")}

Traitement médecin :
{state.get("physician_treatment")}

Ajoute obligatoirement :

"Ce système ne remplace pas une consultation médicale."
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return {
        "final_report": response.content,
        "next": "FINISH"
    }