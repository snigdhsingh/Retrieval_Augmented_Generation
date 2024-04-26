import json
import urllib.request


def load_impact_theory_data():
    try:
        path = "data/impact_theory_data.json"
        with open(path) as f:
            data = json.load(f)
        return data
    except Exception:
        print(f"Data not available at {path}")
