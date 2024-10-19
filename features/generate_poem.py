# File: features/generate_poem.py

import random

def generate_poem():
    subjects = ["love", "nature", "life", "dreams", "time", "hope"]
    adjectives = ["beautiful", "mysterious", "enchanting", "vibrant", "serene", "ethereal"]
    verbs = ["dance", "whisper", "illuminate", "inspire", "flow", "bloom"]
    
    subject = random.choice(subjects)
    adj1, adj2 = random.sample(adjectives, 2)
    verb1, verb2 = random.sample(verbs, 2)
    
    poem = f"""
    In the realm of {subject}, {adj1} and true,
    We {verb1} through moments, both old and new.
    With {adj2} thoughts that {verb2} and rise,
    We find our place beneath the skies.
    """
    return poem