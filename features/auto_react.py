# File: features/auto_react.py

import random

async def auto_react(client):
    reactions = ["👍", "❤️", "😊", "😮", "😂", "🎉", "👏"]

    @client.on_message()
    async def react_to_message(message):
        if random.random() < 0.1:  # 10% chance to react
            reaction = random.choice(reactions)
            await message.react(reaction)
            print(f"Reacted with {reaction} to message from {message.author}")