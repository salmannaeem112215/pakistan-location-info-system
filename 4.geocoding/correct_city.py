import json

# Load files
with open('city_geocoding_local.json', 'r', encoding='utf-8') as f:
    city_data = json.load(f)

with open('missing_city.json', 'r', encoding='utf-8') as f:
    missing_data = json.load(f)

# Build a dict for fast lookup from missing data (using 'name' key)
missing_dict = {item['name']: item for item in missing_data}

# Process and merge
merged_data = []
for item in city_data:
    city_name = item.get('name')
    if city_name in missing_dict:
        merged_data.append(missing_dict[city_name])  # use data from missing_city.json
    else:
        merged_data.append(item)  # keep original

# Save to new JSON
with open('updated_city_geocoding.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print("✅ Merged successfully.")
