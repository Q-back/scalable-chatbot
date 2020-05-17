from fastapi import FastAPI
from pydantic.main import BaseModel


class Question(BaseModel):
    question: str


class Answer(BaseModel):
    question: str
    answer: str


class DefaultAnswer(Answer):
    question: str
    answer: str = "I can't understand you. Please ask me something else."


app = FastAPI()


@app.post('/question/')
def make_question(data: Question):
    if 'hi' in data.question.lower():
        return Answer(question=data.question, answer='hi')
    return DefaultAnswer(question=data.question)
