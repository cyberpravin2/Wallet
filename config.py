import os
from dotenv import load_dotenv

load_dotenv()

# ===== TELEGRAM BOT =====
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ⚠️ HARD-CODED (PRIVATE BOT)
API_ID = 23008482                # <-- yahan apna api_id daalo (number)
API_HASH = "27e2c0dde5c7e1a0cea58446e5262568" # <-- yahan apna api_hash daalo

# ===== DATABASE =====
MONGO_URI = os.getenv("MONGO_URI")

# ===== ADMINS =====
ADMIN_IDS = list(
    map(int, os.getenv("ADMIN_IDS", "").split(","))
) if os.getenv("ADMIN_IDS") else []

# ===== SUPPORT GROUP =====
SUPPORT_GROUP_ID = int(os.getenv("SUPPORT_GROUP_ID", 0))
