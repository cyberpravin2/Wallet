from pyrogram import Client

from config import BOT_TOKEN, API_ID, API_HASH
from handlers import start, wallet, admin, admin_roles

app = Client(
    "monkey_wallet_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

start.register(app)
wallet.register(app)
admin.register(app)
admin_roles.register(app)

print("🐒 Monkey Wallet Bot is running...")
app.run()
