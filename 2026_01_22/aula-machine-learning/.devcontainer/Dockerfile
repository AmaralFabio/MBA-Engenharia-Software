FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# ESSENCIAL para notebooks no VS Code
RUN pip install --upgrade pip \
    && pip install ipykernel

# Container fica rodando
CMD ["sleep", "infinity"]
