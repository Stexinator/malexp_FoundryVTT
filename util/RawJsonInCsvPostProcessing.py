import csv
import json
import re
import os

input_path = "rawdata/weapon_src.csv"
output_path = input_path + ".cleaned"

json_fields = ["JsonDamage", "JsonTraits", "JsonCategory", "JsonSkill", "JsonRange"]

with open(input_path, newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
        # Write header line
        outfile.write(','.join(fieldnames) + '\n')

        for row in reader:
            output_row = []
            for field in fieldnames:
                value = row[field]

                # Strip CSV-escaped quotes from JSON fields
                if field in json_fields:
                    # If it's surrounded by quotes and contains double-double quotes, it's escaped
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1].replace('""', '"')
                    # JSON field should not be quoted at all
                    output_row.append(value)
                else:
                    # Escape value if needed (e.g. contains comma or quote)
                    if ',' in value or '"' in value:
                        value = '"' + value.replace('"', '""') + '"'
                    output_row.append(value)
            outfile.write(','.join(output_row) + '\n')

# Replace original
os.replace(output_path, input_path)
