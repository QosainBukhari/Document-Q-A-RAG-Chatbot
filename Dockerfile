FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

# Install CPU-only torch
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining packages
RUN pip install --default-timeout=1000 --retries 20 --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 8501