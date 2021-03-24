# settings.py
from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.getenv("API_TOKEN")
DEFAULT_PROJECT = os.getenv('DEFAULT_PROJECT')
API_TOKEN = os.getenv('API_TOKEN')
USER_NAME = os.getenv('USER_NAME')
SERVER = os.getenv('SERVER')