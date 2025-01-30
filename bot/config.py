import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("Токен не был найден! Пожалуйста, проверьте файл .env.")