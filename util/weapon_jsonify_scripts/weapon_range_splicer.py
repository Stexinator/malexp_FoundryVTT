import csv
import json
import os

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

def is_melee_range(range_value: str) -> bool:
    return range_value.strip() in ("", "0", "-", "--")

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    # Add new columns if missing
    for col in ("AttackType", "NormalizedRange"):
        if col not in fieldnames:
            fieldnames.append(col)

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        range_raw = row.get("Range", "").strip().lower()

        # Determine if melee
        melee = is_melee_range(range_raw)
        row["AttackType"] = "melee" if melee else "ranged"

        # Store range only if it's ranged
        row["NormalizedRange"] = "" if melee else range_raw

        dictwriter.writerow(row)

# Replace original file with updated version
os.replace(temp_path, input_path)
