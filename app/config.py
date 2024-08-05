from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    APP_NAME: str = os.getenv("APP_NAME")