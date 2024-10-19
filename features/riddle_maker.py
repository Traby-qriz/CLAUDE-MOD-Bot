# File: features/riddle_maker.py

import random

riddles = [
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "answer": "An echo"},
    {"question": "You see a boat filled with people. It has not sunk, but when you look again you don't see a single person on the boat. Why?", "answer": "All the people were married"},
    {"question": "What has keys, but no locks; space, but no room; you can enter, but not go in?", "answer": "A keyboard"},
    {"question": "What gets wet while drying?", "answer": "A towel"},
    {"question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", "answer": "A map"}
]

async def riddle_maker():
    return random.choice(riddles)