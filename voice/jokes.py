import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "How does a penguin build its house? Igloos it together!",
    "Why don't skeletons fight each other? They don't have the guts."
]

def tell_joke():
    joke = random.choice(jokes)
    return joke
