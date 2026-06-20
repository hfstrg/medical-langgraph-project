from app.state import MedicalState


def report_agent(state: MedicalState):

    report = f"""
==============================
RAPPORT CLINIQUE FINAL
==============================

Patient : {state.get("patient_name")}
Âge : {state.get("patient_age")}

Symptômes :
{state.get("symptoms")}

Synthèse clinique :
{state.get("diagnostic_summary")}

Recommandation intermédiaire :
{state.get("interim_care")}

Avis du médecin :
{state.get("physician_treatment")}

--------------------------------
AVERTISSEMENT
--------------------------------
Ce système ne remplace pas une consultation médicale.
"""

    return {
        "final_report": report,
        "next": "FINISH"
    }