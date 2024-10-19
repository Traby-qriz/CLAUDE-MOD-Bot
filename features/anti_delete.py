# File: features/anti_delete.py

deleted_messages = {}

async def anti_delete(client):
    @client.on_message_delete()
    async def handle_delete(message):
        chat_id = message.chat.id
        if chat_id not in deleted_messages:
            deleted_messages[chat_id] = []
        deleted_messages[chat_id].append({
            'author': message.author.name,
            'text': message.text,
            'timestamp': message.timestamp
        })
        print(f"Saved deleted message from {message.author.name}")

async def get_deleted_messages(chat_id):
    return deleted_messages.get(chat_id, [])