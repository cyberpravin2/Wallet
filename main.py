from pyrogram import Client
from config import BOT_TOKEN
from handlers import start, wallet, admin, admin_roles

app = Client(
    "monkey_wallet_bot",
    bot_token=BOT_TOKEN
)

start.register(app)
wallet.register(app)
admin.register(app)
admin_roles.register(app)

print("🐒 Monkey Wallet Bot is running...")
app.run()
