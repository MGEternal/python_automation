import pyautogui

# จับภาพหน้าจอทั้งหมด
screenshot = pyautogui.screenshot()

# บันทึกภาพหน้าจอเป็นไฟล์
screenshot.save('screenshot.png')
