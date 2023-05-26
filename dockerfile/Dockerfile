FROM python:alpine3.17

WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY index.html . 

RUN  pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
