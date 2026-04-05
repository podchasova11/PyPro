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
#
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Указываем путь к папке для загрузок
# download_dir = os.path.abspath("lesson_6/downloads")
#
# # Создаём папку, если её нет
# os.makedirs(download_dir, exist_ok=True)
#
# # Настройки Chrome
# options = Options()
# options.add_experimental_option("prefs", {
#     "download.default_directory": download_dir,
#     "safebrowsing.enabled": False,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "download.extensions_to_open": "",  # предотвращает открытие в браузере
# })
#
# # Инициализация драйвера
# driver = webdriver.Chrome(options=options)
#
# try:
#     # Открываем страницу
#     driver.get("http://the-internet.herokuapp.com/download")
#
#     # Ждём, пока появятся ссылки на файлы (элементы <a>)
#     wait = WebDriverWait(driver, 10)
#     links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='content']//a")))
#
#     print(f"Найдено {len(links)} файлов для скачивания.")
#
#     # Скачиваем только первые 5 файлов
#     for i, link in enumerate(links[:5], 1):
#         try:
#             driver.execute_script("arguments[0].scrollIntoView(true);", link)
#             wait.until(EC.element_to_be_clickable(link))
#             link.click()
#             print(f"[{i}/5] Скачан: {link.text.strip() or 'без имени'}")
#         except Exception as e:
#             print(f"[{i}/5] Ошибка при скачивании: {e}")
#
#     print("Загрузка первых 5 файлов завершена.")
#
# finally:
#     driver.quit()
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 30, poll_frequency=1)
#
#
# driver.get("https://demoqa.com/dynamic-properties")
#
# VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# wait.until(EC.element_to_be_clickable(VISIBLE_AFTER_BUTTON)) # Ждем пока кнопка станет кликабельной
# driver.find_element(*VISIBLE_AFTER_BUTTON).click()


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Настройка драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30, poll_frequency=1)

try:
    driver.get("https://demoqa.com/dynamic-properties")

    # Ожидаем, пока кнопка enableAfter станет кликабельной (видимой + enabled)
    enable_after_button = wait.until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    enable_after_button.click()

    print("✅ Кнопка 'enableAfter' успешно найдена и кликнута.")

finally:
    # закрыть браузер
    driver.quit()
