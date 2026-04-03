from selenium import webdriver
import time
import os
#
#
# FILE_UPLOAD_FIELD = ("xpath", "//input[@id='uploadFile']")
# driver = webdriver.Chrome()
#
# driver.get("https://demoqa.com/upload-download")
#
# # Записываем поле ввода в переменную
# upload_file_field = driver.find_element(*FILE_UPLOAD_FIELD)
#
# # Загружаем картинку
# upload_file_field.send_keys(os.path.join(os.getcwd(), "lesson_6", "img.jpeg"))
#
# time.sleep(5)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By


# Инициализируем опции
options = Options()
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "downloads"),
    "safebrowsing.enabled" : False,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
options.add_experimental_option("prefs", preferences)

# Добавляем опции в браузер
driver = webdriver.Chrome(options=options)

# Открываем страницу для скачивания файлов
driver.get("http://the-internet.herokuapp.com/download")

# Найдем все элементы и кликнем на любой
driver.find_elements(By.XPATH, "//*[@id='content']/div/a[2]']")[1].click()

