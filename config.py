import os
from dotenv import load_dotenv

load_dotenv()

# ===== Telegram =====
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Main admin IDs (comma separated in .env)
ADMIN_IDS = list(
    map(int, os.getenv("ADMIN_IDS", "").split(",")) if os.getenv("ADMIN_IDS") else []
)

# Support group (for disputes)
SUPPORT_GROUP_ID = int(os.getenv("SUPPORT_GROUP_ID", 0))

# ===== Database =====
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "monkey_wallet_bot"

# ===== Wallet rules (fixed logic) =====
WITHDRAW_MIN_AMOUNT = 5     # ₹5 minimum withdraw
