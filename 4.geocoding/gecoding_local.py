import time
import json
import requests
import urllib.parse

# Your Photon server URL
PHOTON_URL = "http://localhost:2322/api"

# Storage lists
found_cities = []
not_found_cities = []

# Read city names from file and process
with open('address.txt') as f:
    for line in f:
        city_name = line.strip()
        try:
            # Build the query URL
            params = {
                'q': f"{city_name}, Pakistan",
                'limit': 1
            }
            url = f"{PHOTON_URL}?{urllib.parse.urlencode(params)}"
            
            # Send request
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error if failed
            
            data = response.json()
            features = data.get("features", [])
            
            if features:
                # Get first feature's coordinates
                coords = features[0]['geometry']['coordinates']
                lon, lat = coords[0], coords[1]
                print(f"Found: {city_name} -> {lat}, {lon}")
                
                found_cities.append({
                    "name": city_name,
                    "geoPoints": [lat, lon]
                })
            else:
                print(f"Not found: {city_name}")
                not_found_cities.append(city_name)
            
        except Exception as e:
            print(f"Error processing {city_name}: {e}")
            not_found_cities.append(city_name)

# Save successful geocodes
with open('address_geocoding_local.json', 'w', encoding='utf-8') as f:
    json.dump(found_cities, f, ensure_ascii=False, indent=4)

# Save not found cities
with open('not_found.json', 'w', encoding='utf-8') as f:
    json.dump(not_found_cities, f, ensure_ascii=False, indent=4)

print("Process completed.")
