# File: features/grab_bio_info.py

async def grab_bio_info(client, user_id):
    try:
        user = await client.get_user_info(user_id)
        return f"Bio: {user.about}"
    except Exception as e:
        return f"Error retrieving bio: {str(e)}"