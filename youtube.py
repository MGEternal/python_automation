from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# เริ่มต้นใช้งาน WebDriver (ในที่นี้ใช้ Chrome WebDriver)
driver = webdriver.Chrome()

# เปิดเว็บ YouTube
driver.get("https://www.youtube.com")

# ค้นหาวิดีโอโดยใส่คำค้นในช่องค้นหา
search_box = driver.find_element("name", "search_query")
search_box.send_keys("ผู้ถูกเลือกให้ผิดหวัง(ดอกไม้ฤดูหนาว) - เรนิษรา (Cover by Palm)")  # เปลี่ยนเป็นคำค้นที่คุณต้องการ
search_box.send_keys(Keys.RETURN)

search_results = driver.find_element("xpath", "ytd-video-renderer")
if search_results:
    # Get the first video element
    first_video = search_results[0]
    print(first_video)
    # Click on the first video
    first_video.click(Keys.RETURN)
else:
    print("No search results found")

# รอให้ผลการค้นหาแสดงผล
# เพิ่มโค้ดอื่น ๆ ที่ต้องการดำเนินการกับผลการค้นหาได้ต่อจากนี้


