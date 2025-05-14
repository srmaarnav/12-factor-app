# Development Setup

## Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Redis

## Local Setup

- **Clone the repository:**

```bash
git clone https://github.com/srmaarnav/12-factor-app.git
cd 12-factor-app
```

- **Create and activate virtual environment:**

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # On Windows: .venv\Scripts\activate
  ```

- **Install dependencies:**

  ```bash
  pip install -r requirements.txt
  ```

- **Set up environment variables:**

  ```bash
  cp .env.example .env
  # Edit .env with your configuration
  ```

- **Run the application:**

  ```bash
  uvicorn app.main:app --reload
  ```

## Docker Setup

- **Build and run with Docker Compose:**

  ```bash
  docker compose up --build
  ```

The API will be available at `http://localhost8000:
