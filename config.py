import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

ADMIN_IDS = list(
    map(int, os.getenv("ADMIN_IDS", "").split(",")) if os.getenv("ADMIN_IDS") else []
)

SUPPORT_GROUP_ID = int(os.getenv("SUPPORT_GROUP_ID", 0))
