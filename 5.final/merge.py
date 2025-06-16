import json

# Load files
with open('pakistan.json', 'r', encoding='utf-8') as f:
    pakistan = json.load(f)

with open('city_geocoding.json', 'r', encoding='utf-8') as f:
    city_geocoding = json.load(f)

with open('address_geocoding.json', 'r', encoding='utf-8') as f:
    address_geocoding = json.load(f)

# Build lookup dicts
city_geocoding_dict = {item['name']: item['geoPoints'] for item in city_geocoding}
address_geocoding_dict = {item['name']: item['geoPoints'] for item in address_geocoding}

result = {}

for province, cities in pakistan.items():
    province_list = []
    for city_entry in cities:
        city_name = city_entry['city']
        city_full_name = f"{city_name}, {province}"
        city_geopoint = city_geocoding_dict.get(city_full_name, [])

        all_list = []
        for address in city_entry.get('all', []):
            full_address_name = f"{address}, {province}"

            # First try address-level geopoint
            geopoint = address_geocoding_dict.get(full_address_name)
            if geopoint is None:
                geopoint = city_geopoint

            all_list.append({
                "name": address,
                "geoPoints": geopoint if geopoint is not None else []
            })

        city_data = {
            "city": city_name,
            "geoPoints": city_geopoint,   # ✅ Add city-level geopoints here
            "all": all_list
        }

        # ✅ If 'popular' exists, add it
        if 'popular' in city_entry:
            city_data['popular'] = city_entry['popular']

        province_list.append(city_data)

    result[province] = province_list

# Save result
with open('geocoding.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print("Done. Saved geocoding.json")
