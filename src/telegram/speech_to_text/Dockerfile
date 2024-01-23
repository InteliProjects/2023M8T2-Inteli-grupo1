FROM python:3.11

WORKDIR /app

COPY stt.py .
COPY .env .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "stt.py"]