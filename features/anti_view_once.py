# File: features/anti_view_once.py

import os

async def anti_view_once(client):
    @client.on_message()
    async def handle_view_once(message):
        if message.is_view_once:
            file_path = await message.download_media()
            new_path = file_path.replace('view_once', 'saved')
            os.rename(file_path, new_path)
            await message.reply("View once media saved!")
            print(f"Saved view once media from {message.author.name}")