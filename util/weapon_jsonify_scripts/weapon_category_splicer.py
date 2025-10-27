import csv
import json
import os

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

# Define keyword map (customize as needed)
category_keywords = {
    "mundane": ["knife", "sword", "axe", "club"],
    "chain": ["chain"],
    "power": ["power"],
    "shock": ["shock"],
    "force": ["force"],
    "bolt": ["bolt"],
    "solid": ["autogun", "solid", "slug", "stub", "gatling", "shotgun", "sniper rifle", "autogun"],
    "las": ["las", "hotshot", "laser"],
    "flame": ["flame"],
    "launcher": ["launcher"],
    "melta": ["melta"],
    "plasma": ["plasma"],
    "specialized": ["needle", "webber", "rad", "grav"],
    "grenadesExplosives": ["grenade", "mine", "charge", "demo", "missile"]
}

def detect_category(description: str) -> str:
    description = description.lower()
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in description:
                return category
    return "" 

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    if "NormalizedCategory" not in fieldnames:
        fieldnames.append("NormalizedCategory")

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        description = row.get("Description", "").strip()
        category = detect_category(description)
        row["NormalizedCategory"] = category
        dictwriter.writerow(row)

# Replace original file
os.replace(temp_path, input_path)
