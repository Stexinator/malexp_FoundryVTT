import csv
import json
import re
import os

# Match patterns like "Rend (3)" or "Loud"
traitRegEx = re.compile(r"([\w\s]+?)(?:\s*\((\d+)\))?$")

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

def normalize_key(key: str) -> str:
    parts = key.strip().lower().split()
    if not parts:
        return ""
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    if "JsonTraits" not in fieldnames:
        fieldnames.append("JsonTraits")

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        traits_list = []

        traits_raw = row.get("Traits", "")
        trait_entries = [t.strip() for t in traits_raw.split(",") if t.strip()]

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

        json_structure = {
            "traits": {
                "list": traits_list
            }
        }

        row["JsonTraits"] = json.dumps(json_structure, ensure_ascii=False)

        dictwriter.writerow(row)

# Replace original file with updated file
os.replace(temp_path, input_path)
