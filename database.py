# database.py
import json
from pathlib import Path

DB_FILE = Path("data.json")

# Başlangıç veri yapısı
data = {
    "users": {},       # user_id: {"country": str, "song": str, "has_voted": False}
    "votes": {},       # target_country: {voter_id: points}
    "vote_order": []   # Oylama sırası
}

# Veriyi yükle
def load_data():
    global data
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            data = json.load(f)

# Veriyi kaydet
def save_data():
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)