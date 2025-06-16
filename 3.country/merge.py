import json
import os
from collections import defaultdict
import glob

# Input files
input_file = 'city.txt'
output_file = 'pakistan.json'

# Use defaultdict to automatically create lists for each province
data = defaultdict(list)

index = 1

with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        try:
            city, province = map(str.strip, line.split(',', 1))
            
            # Create city object
            city_obj = {"city": city}

            # Build pattern for json index file (any file starting with index_)
            pattern = f"./json/{index}_*.json"
            matching_files = glob.glob(pattern)

            if matching_files:
                filename = matching_files[0]  # pick the first match
                try:
                    with open(filename, 'r', encoding='utf-8') as city_file:
                        city_data = json.load(city_file)
                    
                    # Only add popular if exists
                    if "popular" in city_data:
                        city_obj["popular"] = city_data["popular"]
                    
                    # Only add all if exists
                    if "all" in city_data:
                        city_obj["all"] = city_data["all"]
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
            else:
                print(f"No file for index {index}, skipping additional data.")

            data[province].append(city_obj)
            index += 1

        except ValueError:
            print(f"Skipping invalid line: {line}")

# Convert defaultdict to normal dict
data = dict(data)

# Write to JSON file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"JSON file '{output_file}' created successfully.")
