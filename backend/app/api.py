from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import create_graph


app = FastAPI(
    title="Medical Multi-Agent API"
)

graph = create_graph()


class ConsultationInput(BaseModel):

    patient_name: str
    patient_age: int
    symptoms: str


@app.get("/")
def root():

    return {
        "message": "Medical LangGraph API running"
    }


@app.post("/consultation/start")
def start_consultation(data: ConsultationInput):

    initial_state = {
        "patient_name": data.patient_name,
        "patient_age": data.patient_age,
        "symptoms": data.symptoms,
        "question_count": 0,
        "patient_answers": []
    }

    result = graph.invoke(initial_state)

    return result
