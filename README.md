
# Project Title

A brief description of what this project does and who it's for

# FastAPI-Docker

Serving ML models through FastAPI and Docker

##  Overview

This repository provides a streamlined setup to serve machine learning (ML) models using a FastAPI application containerized with Docker. Ideal for deploying models as scalable and reliable REST APIs.

##  Features

- **FastAPI-powered API** – Lightweight, performant, and automatic OpenAPI/Swagger documentation.
- **Dockerized** – Easy to build and run your application in a container.
- **Model integration** – Load and serve a trained ML model from the `model/` directory.
- **Schema validation** – Input/output structures defined under `schema/`.

##  Repository Structure

├── app.py  # Main FastAPI application

├── model/ # Directory for ML model files

├── schema/ # Request/response schema definitions

├── requirements.txt # Python dependencies

├── Dockerfile # Instructions to build Docker image

├── .gitignore # Files/folders to ignore in Git

└── LICENSE # Apache 2.0 open-source license



##  Prerequisites

Make sure you have:
- [Docker](https://docs.docker.com/get-docker/) installed and running.
- A trained ML model saved in `model/` (e.g., `.pkl`, `.pt`, `.joblib`, etc.).

##  Setup & Usage

### Build the Docker image
```bash
docker build -t fastapi-ml-app .

docker run -d --name fastapi-ml -p 8000:80 fastapi-ml-app
```
## Use the API
Open API docs in your browser: http://localhost:8000/docs (Swagger UI).

Alternative docs: http://localhost:8000/redoc.
