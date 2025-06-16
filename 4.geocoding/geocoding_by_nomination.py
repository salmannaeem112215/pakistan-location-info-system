import time
import json
from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="my_app")

# List to store all city geocoding results
city_data = []

# Read city names from file and process
with open('city.txt') as f:
    for line in f:
        city_name = line.strip()
        try:
            location = geolocator.geocode(f"{city_name}, Pakistan")
            if location:
                print(city_name, location.latitude, location.longitude)
                city_entry = {
                    "name": city_name,
                    "geoPoints": [location.latitude, location.longitude]
                }
            else:
                print(city_name, "Not found")
                city_entry = {
                    "name": city_name,
                    "geoPoints": []
                }
            city_data.append(city_entry)
            time.sleep(1.5)  # Sleep to avoid getting banned
        except Exception as e:
            print(city_name, "Error:", e)
            city_entry = {
                "name": city_name,
                "geoPoints": []
            }
            city_data.append(city_entry)

# Save data to JSON file
with open('city_geocoding.json', 'w', encoding='utf-8') as json_file:
    json.dump(city_data, json_file, ensure_ascii=False, indent=4)

print("Geocoding completed and saved to city_geocoding.json")
