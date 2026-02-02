from pyrogram import Client

from bot.config import BOT_TOKEN
from bot.handlers import start, wallet, admin

app = Client(
    "monkey_wallet_bot",
    bot_token=BOT_TOKEN
)

# Register all handlers
start.register(app)
wallet.register(app)
admin.register(app)

print("🐒 Monkey Wallet Bot is running...")
app.run()
