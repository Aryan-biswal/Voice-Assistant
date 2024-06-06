import json
import os

profile_path = 'user_profiles.json'
user_profiles = {}

def load_profiles():
    global user_profiles
    if os.path.exists(profile_path):
        with open(profile_path, 'r') as file:
            user_profiles = json.load(file)

def save_profiles():
    global user_profiles
    with open(profile_path, 'w') as file:
        json.dump(user_profiles, file)

def get_user_profile(user_id):
    return user_profiles.get(user_id, {'name': 'User', 'preferences': {}})

def update_user_profile(user_id, profile):
    user_profiles[user_id] = profile
    save_profiles()

def greet_user(user_id):
    profile = get_user_profile(user_id)
    name = profile.get('name', 'User')
    return f"Hello, {name}! How can I assist you today?"

load_profiles()
