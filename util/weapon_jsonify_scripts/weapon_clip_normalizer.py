import csv
import os

input_path = "rawdata/weapon_src.csv"
temp_path = input_path + ".tmp"

with open(input_path, encoding="utf-8", newline='') as infile, \
     open(temp_path, mode="w", encoding="utf-8", newline='') as outfile:

    dictreader = csv.DictReader(infile)
    fieldnames = dictreader.fieldnames

    if "NormalizedClipValue" not in fieldnames:
        fieldnames.append("NormalizedClipValue")

    dictwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    dictwriter.writeheader()

    for row in dictreader:
        raw_mag = row.get("Mag", "")
        normalMag = raw_mag if raw_mag.isdigit() else ""

        row["NormalizedClipValue"] = normalMag
        dictwriter.writerow(row)

# Replace original file with updated version
os.replace(temp_path, input_path)
