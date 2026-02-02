from pyrogram import Client, filters
from pyrogram.types import Message

from database import users_col, wallet_logs_col


def register(app: Client):

    @app.on_message(filters.command("balance"))
    async def balance_handler(client: Client, message: Message):
        user_id = message.from_user.id

        user = users_col.find_one({"user_id": user_id})

        if not user:
            return await message.reply_text("❌ Please use /start first.")

        balance = user.get("wallet_balance", 0)

        await message.reply_text(
            "🐒 **Monkey Wallet Balance**\n\n"
            f"💰 Balance: ₹{balance}"
        )
