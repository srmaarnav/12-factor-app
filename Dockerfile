FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x scripts/start.sh

ENV PYTHONPATH=/app

CMD ["./scripts/start.sh"]