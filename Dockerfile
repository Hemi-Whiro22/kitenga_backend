FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy to working directory as .env
COPY /kitenga_api/ /app/.env

# Copy config files first (helps Docker layer caching)
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root

# Copy your actual API code
COPY kitenga_api/ /app/kitenga_api/



# Run your app
CMD ["poetry", "run", "uvicorn", "kitenga_api:app", "--host", "0.0.0.0", "--port", "8000"]