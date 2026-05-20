from app.graph import create_graph


graph = create_graph()

result = graph.invoke(
    {
        "patient_name": "Ahmed",
        "patient_age": 35,
        "symptoms": "Fièvre et toux",
        "question_count": 0,
        "patient_answers": []
    }
)

print("\n===== RESULTAT =====\n")
print(result)