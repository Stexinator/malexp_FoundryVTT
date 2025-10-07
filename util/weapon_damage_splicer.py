import csv
import json
import re
import os

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

# Match patterns like "3", "3+StrB", "StrB"
damageRegEx = re.compile(r"^\s*(\d+)?(?:\s*\+?\s*([A-Za-z]\w*))?\s*$")

def normalize_characteristic(raw: str) -> str:
    return raw.strip().lower()[:3] if raw else ""

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    if "JsonDamage" not in fieldnames:
        fieldnames.append("JsonDamage")

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        damage_raw = row.get("Dmg", "").strip()

        # Default structure with all fields
        damage_data = {
            "base": "",
            "characteristic": "",
            "SL": False,
            "ignoreAP": False
        }

        match = damageRegEx.match(damage_raw)
        if match:
            base = match.group(1)
            char_mod = match.group(2)

            if base:
                damage_data["base"] = base  # keep as string
            if char_mod:
                damage_data["characteristic"] = normalize_characteristic(char_mod)

        row["JsonDamage"] = json.dumps({"damage": damage_data}, ensure_ascii=False)
        dictwriter.writerow(row)

# Replace original file with updated version
os.replace(temp_path, input_path)
