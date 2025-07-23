"""
kitenga_backend.kitengas_api.py
"""
from kitenga_backend.scripts.init_card_scan import init_card_scanner as init_card_scanner_tool
from kitenga_backend.kitenga_api.kitenga_awakens import kitenga_awakens 
import os
import pprint
from dotenv import load_dotenv  
import os
import pprint
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()
load_dotenv()
# Get DB connection from env
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"message": "Kitenga lives 🚀"}
@app.get("/init_card_scanner")
def init_card_scanner():
    """
    Initializes the card scanner tool.
    """
    init_card_scanner_tool()
    print("Card scanner initialized successfully.")
    return {"message": "Card scanner initialized successfully."}
@app.get("/kitenga_awakens")
def kitenga_awakens():
    """
    Initializes the Kitenga environment.
    """
    kitenga_awakens()
    print("Kitenga environment initialized successfully.")
    return {"message": "Kitenga environment initialized successfully."}
@app.get("/database_config")
def get_database_config():
    """
    Retrieves the database configuration.
    """
    db_config = {
        "DATABASE_URL": DATABASE_URL,
    }
    return {"database_config": db_config}

if __name__ == "__main__":
    init_card_scanner_tool()
    kitenga_awakens()
    print("🌬️ Kitenga awakens… the awa flows, and the kaitiaki watch.")
    print("The journey begins with the first step into the unknown.")
    print("May the winds guide you, and the waters cleanse your path.")
    print("Kitenga API is ready to serve!")
    print("Card scanner initialized successfully.")
    print("Kitenga environment initialized successfully.")
    print("Database configuration loaded successfully.")
    print("FastAPI server is running.")
