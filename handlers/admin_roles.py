from pyrogram import Client, filters
from pyrogram.types import Message

from bot.permissions import is_admin, ROLE_TASK_ADMIN, ROLE_ADMIN
from bot.database import users_col


def register(app: Client):

    # 🔹 Add Task Admin
    @app.on_message(filters.command("add_task_admin"))
    async def add_task_admin(client: Client, message: Message):
        if not is_admin(message.from_user.id):
            return

        try:
            target_id = int(message.text.split()[1])
        except:
            return await message.reply_text("Usage: /add_task_admin USER_ID")

        result = users_col.update_one(
            {"user_id": target_id},
            {"$set": {"role": ROLE_TASK_ADMIN}}
        )

        if result.matched_count == 0:
            return await message.reply_text("❌ User not found. User must /start first.")

        await message.reply_text(f"✅ User {target_id} promoted to Task Admin")

    # 🔹 Remove Task Admin (back to normal user)
    @app.on_message(filters.command("remove_task_admin"))
    async def remove_task_admin(client: Client, message: Message):
        if not is_admin(message.from_user.id):
            return

        try:
            target_id = int(message.text.split()[1])
        except:
            return await message.reply_text("Usage: /remove_task_admin USER_ID")

        users_col.update_one(
            {"user_id": target_id},
            {"$set": {"role": "user"}}
        )

        await message.reply_text(f"✅ User {target_id} removed from Task Admin role")

    # 🔹 Promote to Main Admin (careful)
    @app.on_message(filters.command("promote_admin"))
    async def promote_admin(client: Client, message: Message):
        if not is_admin(message.from_user.id):
            return

        try:
            target_id = int(message.text.split()[1])
        except:
            return await message.reply_text("Usage: /promote_admin USER_ID")

        users_col.update_one(
            {"user_id": target_id},
            {"$set": {"role": ROLE_ADMIN}}
        )

        await message.reply_text(f"⚠️ User {target_id} promoted to MAIN ADMIN")
