import openai
import os
from os.path import join, dirname
import dotenv
import telebot


dotenv_path = join(dirname(__file__), ".env")
dotenv.load_dotenv(dotenv_path)


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_TOKEN = os.environ.get("OPENAI_TOKEN")
USER_ID = os.environ.get("USER_ID")
USER_NAME = os.environ.get("USER_NAME")


openai.api_key = OPENAI_TOKEN

bot = telebot.TeleBot(str(TELEGRAM_TOKEN))

