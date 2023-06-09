from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver (in this case, using Chrome WebDriver)
driver = webdriver.Chrome()

# Open the YouTube page
driver.get("https://www.youtube.com")

# Find the search input field and enter the search query
search_box = driver.find_element("name", "search_query")
search_query = "ผู้ถูกเลือกให้ผิดหวัง(ดอกไม้ฤดูหนาว) - เรนิษรา (Cover by Palm)"  # Replace with your desired search term
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
search_results_locator = (By.CSS_SELECTOR, "ytd-video-renderer")
search_results = wait.until(EC.visibility_of_all_elements_located(search_results_locator))

pyautogui.click(x=289, y=368)
time.sleep(7)
pyautogui.click(x=828, y=589)
time.sleep(6)
pyautogui.click(x=828, y=589)