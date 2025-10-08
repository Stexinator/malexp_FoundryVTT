import csv
import re
import os

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

# Match ammo cost in parentheses, e.g. "(50)"
ammo_cost_regex = re.compile(r"\((\d+)\)")

# Match initial cost before any parentheses, e.g. "300 (50)" -> "300"
initial_cost_regex = re.compile(r"^\s*(\d+)")

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    # Ensure both columns exist
    for col in ("AmmoCost", "InitialCost"):
        if col not in fieldnames:
            fieldnames.append(col)

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        cost_raw = row.get("Cost", "").strip()

        # Extract initial cost
        initial_match = initial_cost_regex.match(cost_raw)
        initial_cost = initial_match.group(1) if initial_match else "0"

        # Extract ammo cost
        ammo_match = ammo_cost_regex.search(cost_raw)
        ammo_cost = ammo_match.group(1) if ammo_match else "0"

        row["InitialCost"] = initial_cost
        row["AmmoCost"] = ammo_cost

        dictwriter.writerow(row)

# Replace original file with updated version
os.replace(temp_path, input_path)
