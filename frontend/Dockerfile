
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl && apt-get clean
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
