from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27758016"))
API_HASH = getenv("API_HASH", "8d34cfffe27ab461eabbf0091b1a27df")

BOT_TOKEN = getenv("BOT_TOKEN", "7944175084:AAFNDr6fIKd4t__0Nj0yrMtrdXe2vY_FrHs")
OWNER_ID = int(getenv("OWNER_ID", "7224419362"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://architect2002:architect2002@cluster0.ccinu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "The_Architect04")
