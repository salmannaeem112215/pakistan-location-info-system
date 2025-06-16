from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Setup Edge options
options = Options()
# options.add_argument("--headless")  # Uncomment if you want headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")

# Initialize Edge WebDriver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

driver.get("https://www.olx.com.pk/")
wait = WebDriverWait(driver, 15)

# Your specific index list
specific_index = [2, 4, 17, 36, 52, 56, 58, 86, 104, 110, 117, 128, 139, 153, 161, 162, 176, 177, 190, 196, 215, 220, 222, 223, 226]

# Loop over the specific indices
for index in specific_index:
    try:
        ### STEP 1: Click on Location Input
        location_input = wait.until(EC.element_to_be_clickable((By.XPATH,
            '/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[1]/div[1]/input')))
        location_input.click()
        print("Location input field clicked successfully!")
        time.sleep(2)

        ### STEP 2: Try selecting city inside div[5] at current index
        city_option_xpath = f'/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[2]/div[5]/div[{index}]/div/div/span'
        city_option = driver.find_element(By.XPATH, city_option_xpath)
        city_option.click()
        print(f"Clicked city at index {index}")
        time.sleep(2)

        ### STEP 3: Click again on Location Input
        location_input = wait.until(EC.element_to_be_clickable((By.XPATH,
            '/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[1]/div[1]/input')))
        location_input.click()
        print("Clicked input again to reopen dropdown.")
        time.sleep(2)

        ### STEP 4: After everything done, save dropdown HTML
        city_div_updated = driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[2]')
        city_html = city_div_updated.get_attribute('innerHTML')

        filename = f"city_{index}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(city_html)

        print(f"Saved HTML to {filename}")

        ### STEP 5: Click on sub-location
        sub_location_xpath = '/html/body/div/div[1]/header/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/div/span'
        sub_location = wait.until(EC.element_to_be_clickable((By.XPATH, sub_location_xpath)))
        sub_location.click()
        print("Clicked on sub-location span.")
        time.sleep(4)

    except (NoSuchElementException, TimeoutException) as e:
        print(f"No element found at index {index}: {e}")
        continue

    except Exception as e:
        print(f"Unknown error at index {index}: {e}")
        continue

# Finally close the browser after loop finishes
driver.quit()
