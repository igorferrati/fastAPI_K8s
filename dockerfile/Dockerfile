FROM python:3.9

WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY index.html . 

RUN  pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
