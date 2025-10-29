import csv
import json
import os
import re

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

def normalize_skill_name(raw: str) -> str:
    if not raw.strip():
        return ""

    # Remove trailing 's' (simple plural handling)
    raw = raw.strip()
    if raw.lower().endswith("s") and not raw.lower().endswith("ss"):
        raw = raw[:-1]

    # Remove spaces and hyphens, convert to camelCase
    parts = re.split(r"[\s\-]+", raw)
    if not parts:
        return ""

    return parts[0].lower() + ''.join(part.capitalize() for part in parts[1:])

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    if "NormalizedSkill" not in fieldnames:
        fieldnames.append("NormalizedSkill")

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        specialisation = row.get("Specialisation", "")
        skill_name = normalize_skill_name(specialisation)

        row["NormalizedSkill"] = skill_name
        dictwriter.writerow(row)

# Replace original file with updated version
os.replace(temp_path, input_path)
