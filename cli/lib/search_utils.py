import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MOVIES_PATH = PROJECT_ROOT / "data" / "movies.json"


def load_movies() -> list[dict]:
    with open(MOVIES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["movies"]
