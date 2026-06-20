# Medical Multi-Agent Consultation System

## Description

Ce projet présente un système multi-agents d'orientation clinique développé avec LangGraph, FastAPI et Streamlit.

Le système simule un workflow médical composé de plusieurs agents spécialisés :

* Supervisor Agent
* Diagnostic Agent
* Physician Review Agent
* Report Agent

## Technologies utilisées

* Python
* LangGraph
* LangChain
* OpenAI API
* FastAPI
* Streamlit
* Pydantic

## Architecture

Patient → Streamlit → FastAPI → Supervisor → Diagnostic Agent → Physician Review → Report Agent → Rapport Final

## Structure du projet

backend/

* app/

  * api.py
  * graph.py
  * state.py
  * nodes/
  * tools/

frontend/

* app.py

requirements.txt

README.md

## Installation

```bash
pip install -r requirements.txt
```

## Lancement de l'API

```bash
uvicorn app.api:app --reload
```

## Lancement de Streamlit

```bash
streamlit run frontend/app.py
```

## Résultats

Le système collecte les informations du patient, réalise une analyse préliminaire, génère des recommandations et produit un rapport clinique final.

## Auteur

Hafsa Targa

EMSI – Cycle Ingénieur Informatique – IA & Data

Année universitaire 2025-2026
