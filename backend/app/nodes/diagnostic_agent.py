from app.state import MedicalState


def diagnostic_agent(state: MedicalState):

    symptoms = state.get("symptoms", "")

    summary = f"""
Le patient présente les symptômes suivants :
{symptoms}

Analyse préliminaire :
- Les informations ont été collectées.
- Une évaluation médicale complémentaire peut être nécessaire.
- Surveillance recommandée.
"""

    return {
        "diagnostic_summary": summary,
        "interim_care": "Repos, hydratation et surveillance des symptômes.",
        "next": "physician_review"
    }
