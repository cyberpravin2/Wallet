from pyrogram import Client, filters
from permissions import is_admin

def register(app: Client):

    @app.on_message(filters.command("fees"))
    async def fees(client, message):
        if not is_admin(message.from_user.id):
            return
        await message.reply_text("Admin panel active")
