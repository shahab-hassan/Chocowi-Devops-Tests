FROM python:3.10-slim

RUN apt update && \
    apt install -y wget unzip curl gnupg && \
    apt install -y chromium chromium-driver

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]