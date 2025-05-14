#!/bin/bash

# Start mkdocs in background
mkdocs serve --dev-addr=0.0.0.0:8001 &

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000
