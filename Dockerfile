# Resmi Python 3.9 slim tabanlı image kullanılıyor
FROM python:3.9-slim

# Çalışma dizinini belirle
WORKDIR /app

# Bağımlılık dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Tüm uygulama dosyalarını kopyala
COPY . .

# FastAPI'nin çalışacağı portu tanımla
EXPOSE 8000

# Konteyner başlatıldığında uygulamayı calistir
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
