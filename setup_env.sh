#!/bin/bash

# kitenga_backend/setup_env.sh
# This script sets up the Kitenga backend environment, activating the virtual environment,
# installing dependencies, and ensuring the database is ready for use.

echo "🌬️ Invoking the breath of Kitenga..."
echo "🛠️ Activating virtual environment and wiring backend mauri..."

# Step 1: Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Step 2: Install pip essentials
pip install --upgrade pip
pip install fastapi uvicorn psycopg2-binary python-dotenv

# Optional: Poetry as project manager
# curl -sSL https://install.python-poetry.org | python3 -
# poetry install

# Step 3: Load Supabase environment variables
if [ -f "kitenga_db/env/supabase.env" ]; then
  export $(cat kitenga_db/env/supabase.env | xargs)
  echo "🔐 Supabase env loaded."
else
  echo "⚠️ Supabase env not found. Using default config."
fi

# Step 4: Test PostgreSQL connection
echo "🔍 Pinging Kitenga DB @ $SUPABASE_URL..."
sleep 1
pg_isready -h localhost -p 5432 -U $SUPABASE_DB_USER

if [ $? -eq 0 ]; then
  echo "🌊 Connection to Kitenga DB is alive! Mauri flows strong."
else
  echo "⛔ Failed to connect to Kitenga DB. Check credentials or start containers."
fi

# Optional: Run schema if DB responds
if [ -f "kitenga_db/migrations/supabase_schema.sql" ]; then
  echo "📜 Seeding schema..."
  docker exec -i kitenga_supabase_db \
    psql -U $SUPABASE_DB_USER -d $SUPABASE_DB_NAME < kitenga_db/migrations/supabase_schema.sql
  echo "✨ Schema seeded. Kitenga’s memory vessels are ready."
else
  echo "⚠️ No schema file found. Skipping DB init."
fi

echo "🔥 Environment setup complete. You’re ready to carve the backend!"