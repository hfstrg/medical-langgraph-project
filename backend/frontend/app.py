import streamlit as st
import requests

QUESTIONS = [
    "Depuis quand avez-vous ces symptômes ?",
    "Avez-vous de la fièvre ?",
    "Ressentez-vous une douleur particulière ?",
    "Avez-vous des antécédents médicaux ?",
    "Prenez-vous actuellement des médicaments ?"
]

st.set_page_config(
    page_title="Medical Multi-Agent Consultation",
    layout="centered"
)

st.title("🩺 Medical Multi-Agent Consultation")

st.write(
    "Système académique d’orientation clinique préliminaire"
)

# Initialisation session
if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "report" not in st.session_state:
    st.session_state.report = ""

# ==========================
# ETAPE 0 : Infos patient
# ==========================
if st.session_state.step == 0:

    patient_name = st.text_input("Nom du patient")

    patient_age = st.number_input(
        "Âge",
        min_value=0,
        max_value=120,
        value=30
    )

    symptoms = st.text_area("Symptômes")

    if st.button("Démarrer la consultation"):

        st.session_state.patient_name = patient_name
        st.session_state.patient_age = patient_age
        st.session_state.symptoms = symptoms

        st.session_state.step = 1

        st.rerun()

# ==========================
# ETAPES 1 à 5 : Questions
# ==========================
elif st.session_state.step <= 5:

    current_question = QUESTIONS[st.session_state.step - 1]

    st.subheader(
        f"Question {st.session_state.step}/5"
    )

    st.write(current_question)

    answer = st.text_input(
        "Votre réponse",
        key=f"answer_{st.session_state.step}"
    )

    if st.button("Suivant"):

        st.session_state.answers.append(answer)

        # Question suivante
        if st.session_state.step < 5:

            st.session_state.step += 1
            st.rerun()

        # Dernière question terminée
        else:

            payload = {
                "patient_name": st.session_state.patient_name,
                "patient_age": st.session_state.patient_age,
                "symptoms": (
                    st.session_state.symptoms
                    + "\n\nRéponses patient :\n"
                    + "\n".join(st.session_state.answers)
                )
            }

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/consultation/start",
                    json=payload
                )

                result = response.json()

                st.session_state.report = result.get(
                    "final_report",
                    "Aucun rapport généré."
                )

                st.session_state.step = 6

                st.rerun()

            except Exception as e:

                st.error(f"Erreur : {e}")

# ==========================
# ETAPE 6 : Rapport final
# ==========================
elif st.session_state.step == 6:

    st.success("Consultation terminée")

    st.subheader("Rapport Final")

    st.text_area(
        "Résultat",
        st.session_state.report,
        height=400
    )

    if st.button("Nouvelle consultation"):

        st.session_state.step = 0
        st.session_state.answers = []
        st.session_state.report = ""

        st.rerun()