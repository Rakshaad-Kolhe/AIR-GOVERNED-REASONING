from fastapi import FastAPI

from api.routes import process_question


app = FastAPI()


@app.post("/reason")
def reason(payload: dict):
    question = payload.get("question", "")
    response = process_question(question)
    return response.to_dict()
