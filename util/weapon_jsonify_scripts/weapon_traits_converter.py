# INFO: this script is intended to collect trait info from csv and
# convert it into json to fill into the name-matched json pack file of the module
# This is a workaround because complex json formated csv doesn't work well 
# with the CsvImporter module for foundry, so we import with empty traits and then call this script
# to fill up the json pack files with the weapon traits
import os
import json
import csv
import re

# === CONFIGURATION ===
JSON_FOLDER = "packs/malexp_weapons"
CSV_FILE = "rawdata/weapon_src.csv"
traitRegEx = re.compile(r"([\w\s]+?)(?:\s*\((\d+)\))?$") # Match patterns like "Rend (3)" or "Loud"

# Ensure traits have the "correct" malexp foundry system format
def normalize_key(key: str) -> str:
    parts = key.strip().lower().split()
    if not parts:
        return ""
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

# === LOAD CSV INTO DICTIONARY ===
name_to_traits = {}
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row.get("Name")
        traits_str = row.get("Traits")

        traits_list = []
        trait_entries = [t.strip() for t in traits_str.split(",") if t.strip()]

        for trait in trait_entries:
            match = traitRegEx.match(trait)
            if match:
                key_raw = match.group(1)
                key = normalize_key(key_raw)
                value = match.group(2)
                trait_obj = {"key": key}
                if value:
                    trait_obj["value"] = value
                traits_list.append(trait_obj)
        
        name_to_traits[name]  = {"list": traits_list}

# === UPDATE JSON FILES ===
for filename in os.listdir(JSON_FOLDER):
    if not filename.lower().endswith(".json"):
        continue

    file_path = os.path.join(JSON_FOLDER, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    name = data.get("name")
    if name in name_to_traits:
        data["system"]["traits"] = name_to_traits[name]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ Updated {filename} with Traits for '{name}'")
    else:
        print(f"⚠️ No matching Traits found for '{name}' in {filename}")
