def get_mcp_recommendation(symptoms: str):

    if "fièvre" in symptoms.lower():

        return (
            "MCP : Hydratation et surveillance "
            "de la température."
        )

    if "toux" in symptoms.lower():

        return (
            "MCP : Surveillance respiratoire."
        )

    return (
        "MCP : Consultation recommandée "
        "si aggravation."
    )