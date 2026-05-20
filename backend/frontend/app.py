import streamlit as st
import requests


st.set_page_config(
    page_title="Medical Multi-Agent System",
    layout="centered"
)

st.title("🩺 Medical Multi-Agent Consultation")

st.write(
    "Système académique d’orientation clinique préliminaire"
)

patient_name = st.text_input("Nom du patient")

patient_age = st.number_input(
    "Âge",
    min_value=0,
    max_value=120,
    value=30
)

symptoms = st.text_area(
    "Symptômes"
)


if st.button("Démarrer la consultation"):

    payload = {
        "patient_name": patient_name,
        "patient_age": patient_age,
        "symptoms": symptoms
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/consultation/start",
            json=payload
        )

        result = response.json()

        st.success("Consultation terminée")

        st.subheader("Rapport Final")

        st.write(result.get("final_report"))

    except Exception as e:

        st.error(f"Erreur : {e}")