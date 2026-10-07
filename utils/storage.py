import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")


def save(filename, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, filename), "w") as f:
        json.dump(data, f, indent=4)


def load(filename, default):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        save(filename, default)
        return default
    try:
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError:
        return default
