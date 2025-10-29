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

    if "BaseDamage" not in fieldnames:
        fieldnames.append("BaseDamage")
    if "StatDamage" not in fieldnames:
        fieldnames.append("StatDamage")

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        damage_raw = row.get("Dmg", "").strip()
        match = damageRegEx.match(damage_raw)
        if match:
            base = match.group(1)
            char_mod = match.group(2)

            if base:
                row["BaseDamage"] = base
            if char_mod:
                row["StatDamage"] = normalize_characteristic(char_mod)

        dictwriter.writerow(row)

# Replace original file with updated version
os.replace(temp_path, input_path)
