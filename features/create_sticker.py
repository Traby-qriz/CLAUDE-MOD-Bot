# File: features/create_sticker.py

from PIL import Image
import os

async def create_sticker(image_path):
    try:
        img = Image.open(image_path)
        img.thumbnail((512, 512))
        sticker_path = os.path.splitext(image_path)[0] + "_sticker.webp"
        img.save(sticker_path, "WEBP")
        return sticker_path
    except Exception as e:
        return f"Error creating sticker: {str(e)}"