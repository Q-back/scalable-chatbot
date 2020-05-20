FROM python:3.8
WORKDIR app/
COPY . /app
RUN pip install poetry
RUN poetry install
EXPOSE 80
CMD poetry run uvicorn main:app --port 80 --host 0.0.0.0

