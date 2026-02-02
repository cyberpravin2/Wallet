import os
from dotenv import load_dotenv

load_dotenv()

# ===== Telegram =====
BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = list(
    map(int, os.getenv("ADMIN_IDS", "").split(",")) if os.getenv("ADMIN_IDS") else []
)

SUPPORT_GROUP_ID = int(os.getenv("SUPPORT_GROUP_ID", 0))

# ===== Database =====
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "monkey_wallet_bot"

# ===== Wallet Rules =====
WITHDRAW_MIN_AMOUNT = 5  # ₹5 minimum withdraw
