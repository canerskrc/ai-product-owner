#!/bin/bash

# Test ortamı değişkenlerini ayarla
export TESTING=1
export DATABASE_URL="sqlite:///./test.db"

# Test veritabanını temizle
rm -f test.db

# Testleri çalıştır
pytest tests/ -v --cov=app --cov-report=term-missing

# Test veritabanını temizle
rm -f test.db 