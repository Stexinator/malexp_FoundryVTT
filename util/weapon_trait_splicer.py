import csv
import re
import json

# Match patterns like "Rend (3)" or "Loud"
traitRegEx = re.compile(r"([\w\s]+?)(?:\s*\((\d+)\))?$")

output = []

with open("rawdata/weapon_src.csv", encoding="utf-8", newline='') as csvfile:
    dictreader = csv.DictReader(csvfile)
    for row in dictreader:
        traits_list = []

        # Assuming the column is named exactly "Traits"
        traits_raw = row.get("Traits", "")
        trait_entries = [t.strip() for t in traits_raw.split(",") if t.strip()]

        for trait in trait_entries:
            match = traitRegEx.match(trait)
            if match:
                key = match.group(1).strip().lower().replace(" ", "")  # normalize to camelCase-ish
                value = match.group(2)
                trait_obj = {"key": key}
                if value:
                    trait_obj["value"] = value
                traits_list.append(trait_obj)

        output.append({
            "traits": {
                "list": traits_list
            }
        })

# Pretty print the result
print(json.dumps(output, indent=2))