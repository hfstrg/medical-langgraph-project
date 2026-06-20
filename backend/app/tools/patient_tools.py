QUESTIONS = [
    "Depuis quand avez-vous ces symptômes ?",
    "Avez-vous de la fièvre ?",
    "Ressentez-vous une douleur particulière ?",
    "Avez-vous des antécédents médicaux ?",
    "Prenez-vous actuellement des médicaments ?"
]


def ask_patient(question_count: int):

    if question_count < len(QUESTIONS):
        return QUESTIONS[question_count]

    return None