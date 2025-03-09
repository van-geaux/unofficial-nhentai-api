FROM python:3.11-slim

WORKDIR /app

COPY main.py config.yml merge_database.py requirements.txt .gitignore LICENSE ./
COPY src/ src/

RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
