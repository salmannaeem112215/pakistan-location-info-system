import json
import requests
import time

# Your Google Geocoding API Key
API_KEY = 'API_KEY'

# Input file containing list of addresses
INPUT_FILE = 'not_found.json'
OUTPUT_FILE = 'not_found_address_geocoding.json'

# Load the addresses from input JSON
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    addresses = json.load(f)

results = []

for address in addresses:
    # Build request URL
    print("HI")
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={requests.utils.quote(address)}&key={API_KEY}'

    # Send request
    response = requests.get(url)
    print("RESPONSED")
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        geopoint = [round(location['lat'], 5), round(location['lng'], 5)]  # rounding to 5 decimal places for simplicity
        result = {
            "name": address,
            "geopoint": geopoint
        }
        results.append(result)
    else:
        print(f"Failed to geocode address: {address}, Status: {data['status']}")

    time.sleep(0.1)  # polite delay to avoid hitting rate limits

# Save results to output JSON file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Geocoding completed and saved to", OUTPUT_FILE)
