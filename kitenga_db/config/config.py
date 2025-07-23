# config.py

"""kitenga_backend.kitenga_db.config.config.py
This module contains the configuration settings for the Kitenga database.
"""

from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
def get_database_config():
    """
    Returns the database configuration as a dictionary.
    """
    return {
        "url": DATABASE_URL,
        "name": DATABASE_NAME,
        "user": DATABASE_USER,
        "password": DATABASE_PASSWORD,
        "host": DATABASE_HOST,
        "port": DATABASE_PORT
    }
def print_database_config():
    """
    Prints the database configuration to the console.
    """
    config = get_database_config()
    print("Database Configuration:")
    for key, value in config.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    print_database_config()
    get_database_config()
