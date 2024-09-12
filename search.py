from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
from fake_useragent import UserAgent
from pathlib import Path

# Function to perform the search and save a screenshot of the first page results
def search_novamar_insurance(config_name, screenshot_dir):
    # Configure Selenium to use a clean browser profile
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-webrtc")  # Disable WebRTC
    ua = UserAgent()
    options.add_argument(f"user-agent={ua.random}")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Novamar Insurance")
    search_box.submit()
    time.sleep(random.uniform(2, 5))  # Random delay to mimic human behavior

    # Save a screenshot of the entire first page results
    screenshot_path = screenshot_dir / f"{config_name}_search_results.png"
    driver.save_screenshot(str(screenshot_path))
    driver.delete_all_cookies()  # Clear cookies after each search

    driver.quit()

    print(f"Screenshot of the first page results saved as {screenshot_path}")
