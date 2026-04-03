from selenium import webdriver
import time
import os


FILE_UPLOAD_FIELD = ("xpath", "//input[@id='uploadFile']")
driver = webdriver.Chrome()

driver.get("https://demoqa.com/upload-download")

# Записываем поле ввода в переменную
upload_file_field = driver.find_element(*FILE_UPLOAD_FIELD)

# Загружаем картинку
upload_file_field.send_keys(os.path.join(os.getcwd(), "file", "img.jpeg"))

time.sleep(5)
