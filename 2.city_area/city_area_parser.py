import os
import json
import re
from bs4 import BeautifulSoup

# Input and output folders
input_folder = "html"
output_folder = "json"

# Make sure output directory exists
os.makedirs(output_folder, exist_ok=True)


# Helper function to parse each file
def parse_file(input_path):
    with open(input_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Extract city name from "All in {X}" span
    city_span = soup.find("span", string=lambda text: text and text.startswith("All in "))
    if city_span:
        city_name = city_span.text.replace("All in ", "").strip()
    else:
        city_name = "UnknownCity"

    # Find Popular section
    popular_list = []
    all_list = []

    # Find the Popular section start
    popular_header = soup.find("span", string="Popular")

    if popular_header:
        container = popular_header.find_parent().find_next_sibling()
        while container:
            all_in_span = container.find("span", string=lambda text: text and text.startswith("All in "))
            if all_in_span:
                break

            spans = container.find_all("span", class_="a1c1940e")
            for span in spans:
                popular_list.append(span.text.strip())
            container = container.find_next_sibling()

    # After "All in" extract rest for all_list
    if city_span:
        container = city_span.find_parent().find_next_sibling()
        while container:
            spans = container.find_all("span", class_="a1c1940e")
            for span in spans:
                all_list.append(span.text.strip())
            container = container.find_next_sibling()

    data = {
        "city": city_name,
        "popular": popular_list,
        "all": all_list
    }
    return data, city_name

# Helper function to extract number from filename
def extract_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else -1

# Get all html files and sort them numerically
files = [f for f in os.listdir(input_folder) if f.endswith(".html")]
files.sort(key=extract_number)

# Now proper counting
index = 1
unkowns=[]
for filename in files:
    input_path = os.path.join(input_folder, filename)
    data, city_name = parse_file(input_path)
    if(city_name!='UnknownCity'):
        # Clean city_name to be file-system friendly
        safe_city = city_name.replace(" ", "_").replace(",", "")

        output_filename = f"{index}_{safe_city}.json"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

        print(f"Parsed: {filename} → {output_filename}")
    else:
        print(f"Skip: {filename} ")

    index += 1

print("All files processed.")
print("Not Found ")
print(unkowns)

