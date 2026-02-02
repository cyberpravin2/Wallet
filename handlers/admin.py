from pyrogram import Client, filters
from pyrogram.types import Message
from permissions import is_admin
from utils.settings import (
    set_task_upload_fee,
    set_withdraw_fee_percent,
    get_task_upload_fee,
    get_withdraw_fee_percent
)

def register(app: Client):

    @app.on_message(filters.command("fees"))
    async def fees(client: Client, message: Message):
        if not is_admin(message.from_user.id):
            return
        await message.reply_text(
            f"🐒 Monkey Wallet Fees\n\n"
            f"Task Upload Fee: ₹{get_task_upload_fee()}\n"
            f"Withdraw Fee: {get_withdraw_fee_percent()}%"
        )

    @app.on_message(filters.command("set_task_fee"))
    async def set_task_fee(client: Client, message: Message):
        if not is_admin(message.from_user.id):
            return
        try:
            amount = int(message.text.split()[1])
        except:
            return await message.reply_text("Usage: /set_task_fee 2")
        set_task_upload_fee(amount)
        await message.reply_text(f"✅ Task upload fee set to ₹{amount}")

    @app.on_message(filters.command("set_withdraw_fee"))
    async def set_withdraw_fee(client: Client, message: Message):
        if not is_admin(message.from_user.id):
            return
        try:
            percent = int(message.text.split()[1])
        except:
            return await message.reply_text("Usage: /set_withdraw_fee 2")
        set_withdraw_fee_percent(percent)
        await message.reply_text(f"✅ Withdraw fee set to {percent}%")
