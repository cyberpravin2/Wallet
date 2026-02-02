from pyrogram import Client, filters
from database import users_col

def register(app: Client):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message):
        user_id = message.from_user.id
        username = message.from_user.username

        user = users_col.find_one({"user_id": user_id})
        if not user:
            users_col.insert_one({
                "user_id": user_id,
                "username": username,
                "wallet_balance": 0,
                "role": "user"
            })
            await message.reply_text("🐒 Welcome! Wallet created with ₹0 balance.")
        else:
            await message.reply_text(
                f"🐒 Welcome back!\nBalance: ₹{user.get('wallet_balance', 0)}"
            )
