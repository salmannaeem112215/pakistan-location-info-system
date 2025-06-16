from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = Options()
# options.add_argument("--headless")  # Uncomment this if you want headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

# Start WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open OLX website
driver.get("https://www.olx.com.pk/")

wait = WebDriverWait(driver, 15)

try:
    # 1️⃣ Click the input field
    location_input = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[1]/div[1]/input'
    )))
    
    location_input.click()
    print("Location input field clicked successfully!")

    # 2️⃣ Wait for 5 seconds
    time.sleep(5)

    # 3️⃣ Now find the dropdown full div
    dropdown_div = driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[2]')

    # 4️⃣ Get the inner HTML content
    dropdown_html = dropdown_div.get_attribute('innerHTML')

    # 5️⃣ Save it to city.txt file
    with open("city.html", "w", encoding="utf-8") as f:
        f.write(dropdown_html)

    print("Dropdown HTML saved to city.txt")

except Exception as e:
    print("Error:", e)

driver.quit()
