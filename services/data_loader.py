import json

def load_current_data():
    with open("data/city_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_history_data():
    with open("data/city_history.json", "r", encoding="utf-8") as f:
        return json.load(f)