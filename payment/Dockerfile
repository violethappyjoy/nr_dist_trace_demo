# gateway/Dockerfile (same for cart, payment)
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Common New Relic defaults; app name and license come from env at runtime
# ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true \
#     NEW_RELIC_LOG=stdout \
#     NEW_RELIC_LOG_LEVEL=info \
#     NEW_RELIC_AGENT_ENABLED=true

EXPOSE 5000

# Use gunicorn for a more realistic production-style server
CMD ["gunicorn", "-b", "0.0.0.0:5002", "app:app"]