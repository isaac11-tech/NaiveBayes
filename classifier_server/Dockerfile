FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY classifier.py .
COPY ../requests%20classifier.py .


CMD ["python", "client-side.py"]