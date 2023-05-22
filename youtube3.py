from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import numpy as np
from PIL import ImageGrab

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

template = cv2.imread('capture.png', 0)  # ใส่ชื่อไฟล์รูปที่ต้องการจับ
time.sleep(7)

while True:
    # จับภาพหน้าจอ
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    
    # ทำการค้นหาภาพที่ตรงกับรูปภาพที่ต้องการคลิก
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # กำหนดค่า threshold สำหรับการค้นหาภาพ
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    
    # คลิกที่ภาพที่ตรงกับรูป
    for loc in locations:
        top_left = loc
        pyautogui.click(top_left[0], top_left[1])
    
    # หยุดการทำงานเมื่อกด 'q' บนคีย์บอร์ด
    if cv2.waitKey(1) == ord('q'):
        break

# คืนค่าหน่วยความจำที่ใช้
cv2.destroyAllWindows()