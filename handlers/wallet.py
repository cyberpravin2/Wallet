from pyrogram import Client, filters
from database import users_col

def register(app: Client):

    @app.on_message(filters.command("balance"))
    async def balance_handler(client, message):
        user = users_col.find_one({"user_id": message.from_user.id})
        if not user:
            return await message.reply_text("Use /start first")

        await message.reply_text(
            f"💰 Your balance: ₹{user.get('wallet_balance', 0)}"
        )
