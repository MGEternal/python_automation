from selenium import webdriver

# ระบุที่อยู่ของ ChromeDriver
chrome_driver_path = 'chromedriver'

# เรียกใช้ WebDriver ของเบราว์เซอร์ Chrome และระบุที่อยู่ของ ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# เปิดเว็บไซต์ YouTube
driver.get("https://www.youtube.com")
