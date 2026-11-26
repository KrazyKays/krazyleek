#!/usr/bin/env python3
"""Télécharge les données publiques de l'API Leek Wars dans docs/data/.

Usage : python3 tools/fetch_api_data.py
Données : puces, armes, constantes et fonctions LeekScript (aucune authentification).
"""
import json
import pathlib
import urllib.request

API = "https://leekwars.com/api/"
ENDPOINTS = {
    "chips": "chip/get-all",
    "weapons": "weapon/get-all",
    "constants": "constant/get-all",
    "functions": "function/get-all",
}
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "data"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, endpoint in ENDPOINTS.items():
        with urllib.request.urlopen(API + endpoint, timeout=30) as resp:
            data = json.load(resp)
        path = OUT / f"{name}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True))
        print(f"{name}: {path.relative_to(OUT.parent.parent)}")


if __name__ == "__main__":
    main()
