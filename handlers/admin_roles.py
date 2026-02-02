from pyrogram import Client, filters
from bot.permissions import is_admin, ROLE_TASK_ADMIN
from database import users_col

def register(app: Client):

    @app.on_message(filters.command("add_task_admin"))
    async def add_task_admin(client, message):
        if not is_admin(message.from_user.id):
            return

        try:
            uid = int(message.text.split()[1])
        except:
            return await message.reply_text("Usage: /add_task_admin USER_ID")

        users_col.update_one(
            {"user_id": uid},
            {"$set": {"role": ROLE_TASK_ADMIN}}
        )

        await message.reply_text("✅ Task Admin added")
