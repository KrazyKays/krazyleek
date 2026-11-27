#!/usr/bin/env python3
"""Télécharge les données publiques de l'API Leek Wars dans docs/data/.

Usage : python3 tools/fetch_api_data.py
Données : puces, armes, constantes, fonctions LeekScript, objets (prix), composants (encyclopédie).
Aucune authentification.
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
    "items": "item/get-all",
}
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "data"


def fetch_components():
    """Composants : page « Components » de l'encyclopédie (niveau, apports, recette)."""
    import re
    with urllib.request.urlopen(API + "encyclopedia/get/en/Components", timeout=30) as resp:
        text = json.load(resp)["content"]
    text = re.sub(r'<img[^>]*alt="([^"]+)"[^>]*/?>', r"[\1]", text).replace("\xa0", " ")
    comps = []
    for m in re.finditer(r"\*\*Level (\d+): ([^*]+)\*\*[^\n]*\nGives: ([^\n]*)\nResources needed to craft: ([^\n]*)", text):
        gives = [g.strip() for g in m.group(3).split("|")]
        comps.append({"level": int(m.group(1)), "name": m.group(2).strip(), "gives": gives,
                      "recipe": m.group(4).strip()})
    return {"components": comps}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "components.json").write_text(json.dumps(fetch_components(), ensure_ascii=False, indent=1))
    print("components: docs/data/components.json")
    for name, endpoint in ENDPOINTS.items():
        with urllib.request.urlopen(API + endpoint, timeout=30) as resp:
            data = json.load(resp)
        path = OUT / f"{name}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True))
        print(f"{name}: {path.relative_to(OUT.parent.parent)}")


if __name__ == "__main__":
    main()
