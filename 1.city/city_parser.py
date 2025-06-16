from bs4 import BeautifulSoup

# Load HTML from file
with open("city.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Select all top-level divs
all_divs = soup.find_all("div", recursive=False)

# Select the last div
if all_divs:
    last_div = all_divs[-1]

    # Inside last_div, find all spans
    spans = last_div.find_all("span")

    # Extract text from each span
    cities = []
    for span in spans:
        city_name = span.get_text(strip=True)
        cities.append(city_name)
        print(city_name)  # For verification

    # Save to city.txt
    with open("city.txt", "w", encoding="utf-8") as f:
        for city in cities:
            f.write(city + "\n")

    print("Cities saved to city.txt")

else:
    print("No divs found in HTML!")
