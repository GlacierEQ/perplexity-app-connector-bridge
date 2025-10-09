FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app_connector_bridge.py .

EXPOSE 8080

CMD ["python", "app_connector_bridge.py"]