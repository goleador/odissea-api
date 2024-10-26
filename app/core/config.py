# app/core/config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Settings:
    TWILIO_SID: str = os.getenv("TWILIO_SID")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()