from pyrogram import Client
from bot.config import BOT_TOKEN
from bot.handlers import admin

app = Client(
    "monkey_wallet_bot",
    bot_token=BOT_TOKEN
)

admin.register(app)

print("🐒 Monkey Wallet Bot started...")
app.run()
