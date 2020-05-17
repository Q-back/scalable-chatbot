from fastapi import FastAPI
from pydantic.main import BaseModel


class Question(BaseModel):
    question: str


class Answer(BaseModel):
    question: str
    answer: str


class DefaultAnswer(Answer):
    answer: str = "I can't understand you. Please ask me something else."


app = FastAPI()


@app.post('/question/')
def make_question(data: Question):
    question_words = data.question.lower().split()
    if 'hi' in question_words:
        return Answer(question=data.question, answer='hi')
    if 'can' in question_words:
        return Answer(question=data.question, answer="I can barely speak. Can't I?")
    if 'what is love?' in data.question.lower():
        return Answer(question=data.question, answer="BABY DON'T HURT ME!")
    return DefaultAnswer(question=data.question)
