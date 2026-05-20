from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MedicalTools")


@mcp.tool()
def get_basic_recommendation(symptom: str) -> str:

    symptom = symptom.lower()

    if "fièvre" in symptom:
        return (
            "Hydratation, repos et surveillance "
            "de la température."
        )

    if "toux" in symptom:
        return (
            "Surveiller la respiration et boire "
            "beaucoup d’eau."
        )

    return (
        "Consulter un professionnel de santé "
        "si les symptômes persistent."
    )


if __name__ == "__main__":

    mcp.run()