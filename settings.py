import os
from dotenv import load_dotenv


load_dotenv()


APPLICATION_SECRET_KEY = os.getenv("SECRET_KEY")
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
