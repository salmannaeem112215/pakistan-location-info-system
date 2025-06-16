import json

# Load the data
with open('pakistan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

output_lines = []

# Process each province
for province, cities in data.items():
    for city_entry in cities:
        city = city_entry.get('city')
        all_places = city_entry.get('all', [])

        if all_places and len(all_places) > 0:
            for place in all_places:
                output_lines.append(f"{place}, {province}")
            # output_lines.append(f"{city}, {province}")

# Save to address.txt
with open('address.txt', 'w', encoding='utf-8') as f:
    for line in output_lines:
        f.write(line + '\n')

print("Extraction completed successfully!")
