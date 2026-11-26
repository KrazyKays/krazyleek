#!/usr/bin/env python3
"""Vérifie que les constantes et fonctions appelées dans ai/**/*.leek existent dans l'API Leek Wars.

Usage : python3 tools/check_api.py [fichiers...]
Utilise docs/data/ (rafraîchir avec tools/fetch_api_data.py).
Limites : analyse par regex (pas un vrai parseur) ; les fonctions et globales
définies dans les fichiers analysés sont reconnues automatiquement.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "data"
KEYWORDS = {"if", "while", "for", "return", "function", "include", "new", "class", "constructor"}


def strip_comments_and_strings(src):
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"//[^\n]*", "", src)
    return re.sub(r'"(\\.|[^"\\])*"', '""', src)


def show(path):
    return path.relative_to(ROOT) if path.is_relative_to(ROOT) else path


def main(paths):
    constants = {c["name"]: c for c in json.loads((DATA / "constants.json").read_text())["constants"]}
    functions = {}
    for f in json.loads((DATA / "functions.json").read_text())["functions"]:
        functions.setdefault(f["name"], []).append(f)

    by_id = {f["id"]: f["name"] for fs in functions.values() for f in fs}
    files = [pathlib.Path(p).resolve() for p in paths] or sorted((ROOT / "ai").rglob("*.leek"))
    sources = {p: strip_comments_and_strings(p.read_text()) for p in files}
    all_src = "\n".join(sources.values())
    user_funcs = set(re.findall(r"\bfunction\s+(\w+)", all_src))
    user_vars = set(re.findall(r"\b(?:global|var)\s+(\w+)", all_src))

    errors = 0
    for path, src in sources.items():
        for lineno, line in enumerate(src.splitlines(), 1):
            for name in re.findall(r"\b([A-Z][A-Z0-9_]{2,})\b", line):
                if name not in constants and name not in user_vars:
                    print(f"{show(path)}:{lineno}: constante inconnue {name}")
                    errors += 1
                elif constants.get(name, {}).get("deprecated"):
                    print(f"{show(path)}:{lineno}: constante dépréciée {name}")
            for name in re.findall(r"\b([a-z]\w*)\s*\(", line):
                if name in KEYWORDS or name in user_funcs:
                    continue
                if name not in functions:
                    print(f"{show(path)}:{lineno}: fonction inconnue {name}()")
                    errors += 1
                elif all(f.get("deprecated") for f in functions[name]):
                    repl = by_id.get(functions[name][0].get("replacement"), "?")
                    print(f"{show(path)}:{lineno}: fonction dépréciée {name}() → {repl}")
    print("OK" if errors == 0 else f"{errors} problème(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
