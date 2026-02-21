import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USER_ID = "pNAMkP8AAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={USER_ID}&hl=en"

OUT_DIR = Path("assets/scholar_badges")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def make_badge_json(label: str, message: str):
    return {"schemaVersion": 1, "label": label, "message": message, "color": "blue"}

def extract_metrics(html: str):
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", {"id": "gsc_rsb_st"}) or soup.find("table", class_="gsc_rsb_st")
    if table is None:
        raise RuntimeError("Could not find metrics table on Google Scholar page.")

    rows = table.find_all("tr")
    metrics = {}
    for r in rows:
        cols = r.find_all(["td", "th"])
        if len(cols) >= 2:
            key = cols[0].get_text(strip=True).lower()
            val = cols[1].get_text(strip=True)  # "All" column
            val = re.sub(r"[^\d]", "", val) or val
            metrics[key] = val

    citations = metrics.get("citations")
    hindex = metrics.get("h-index") or metrics.get("h index")
    i10 = metrics.get("i10-index") or metrics.get("i10 index")

    if not (citations and hindex and i10):
        raise RuntimeError(f"Could not parse all metrics. Parsed keys: {list(metrics.keys())}")

    return citations, hindex, i10

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; GitHubActions/1.0; +https://github.com/)"
    }
    r = requests.get(PROFILE_URL, headers=headers, timeout=30)
    r.raise_for_status()

    citations, hindex, i10 = extract_metrics(r.text)

    (OUT_DIR / "citations.json").write_text(json.dumps(make_badge_json("Citations", citations)), encoding="utf-8")
    (OUT_DIR / "hindex.json").write_text(json.dumps(make_badge_json("h-index", hindex)), encoding="utf-8")
    (OUT_DIR / "i10index.json").write_text(json.dumps(make_badge_json("i10-index", i10)), encoding="utf-8")

    print("Saved:", citations, hindex, i10)

if __name__ == "__main__":
    main()
