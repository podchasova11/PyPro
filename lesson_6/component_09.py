# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# # Locator (improved: use By.XPATH instead of raw tuple)
# VISIBLE_AFTER_BUTTON = ("xpath", "//div[@id='delayedText']")
# DISAPPEARS_TEXT = ("xpath", "//div[@id='deletesuccess']")
# CLICKABLE_BUTTON = ("xpath", "//input[@id='timerButton']")
# TRY_IT_BUTTON = ("xpath", "//button[text()='Try it']")
# MY_BUTTON = ("xpath", "//button[@id='myBtn']")
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("--window-size=1920,1080")  # 'add_argument'
#
# driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver, 30, poll_frequency=1)
#
# try:
#     driver.get("https://omayo.blogspot.com/")
#
#     # Wait to become *invisiblity*
#     wait.until(EC.invisibility_of_element_located(DISAPPEARS_TEXT))
#     print("✅ Text invisiblity successfully.")
#
#     # Wait for the button to become *visible* (not just present)
#     wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
#
#     print("✅ Button [VISIBLE_AFTER_BUTTON] visible successfully.")
#
#     # # Wait button to become *clickable*
#     wait.until(EC.element_to_be_clickable(CLICKABLE_BUTTON))  # Ждем пока кнопка станет кликабельной (видимой + enabled)
#
#     print("✅ Button [CLICKABLE_BUTTON] to become *clickable* successfully.")
#
#     # # Wait button  [TRY_IT_BUTTON] to become *clickable*
#     wait.until(EC.element_to_be_clickable(TRY_IT_BUTTON)).click()  # Ждем пока кнопка станет кликабельной (видимой + enabled)
#
#     print("✅ Button [TRY_IT_BUTTON] to become *clickable* successfully.")
#
#     # Ждем, пока атрибут 'disabled' элемента станет равным "true"
#     wait.until(lambda driver: driver.find_element(*MY_BUTTON).get_attribute("disabled") == "true")
#
#     print("✅ Button [MY_BUTTON] to become disabled")
#
#
# finally:
#     driver.quit()



# import json
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.freeconferencecall.com/login")
# driver.delete_all_cookies()
#
# driver.add_cookie({
#     'username': 'user123'
# })
# driver.refresh()
# # Загружаем cookies из файла
# with open("cookies.json", "r") as f:
#     cookies = json.load(f)
#
# # Обработка ошибок и expiry
# for cookie in cookies:
#     driver.add_cookie(cookie)
#
# driver.refresh()
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Настройка драйвера
# options = Options()
# driver = webdriver.Chrome(options=options)
#
# try:
#     # 1. Открываем сайт
#     driver.get("https://www.freeconferencecall.com/login")
#
#     # 2. Удаляем все существующие куки
#     driver.delete_all_cookies()
#
#     # 3. Устанавливаем куку username=user123
#     driver.add_cookie({
#         "name": "username",
#         "value": "user123",
#         "domain": ".freeconferencecall.com",  # важно: указать домен
#     })
#
#     # 4. Обновляем страницу
#     driver.refresh()
#
#     # 5. Читаем и проверяем куку
#     cookie = driver.get_cookie("username")
#     if cookie:
#         print("✅ Кука 'username' успешно установлена:")
#         print(f"   Значение: {cookie['value']}")
#         print(f"   Домен: {cookie.get('domain', 'не указан')}")
#     else:
#         print(" Кука 'username' не найдена. Возможно, домен или путь указаны неверно.")
#
#     # Дополнительно: вывод всех кук для отладки
#     all_cookies = driver.get_cookies()
#     print(f"\n Всего кук на странице: {len(all_cookies)}")
#     for c in all_cookies:
#         if c["name"] == "username":
#             print(f"   → username = '{c['value']}'")
#
# finally:
#     driver.quit()  # закрываем браузер

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome(options=options)
try:
    driver.get("https://www.freeconferencecall.com/login")

    # 1. Удаляем конкретную cookie по имени:
    # Сначала получаем текущие cookies,
    all_cookies = driver.get_cookies()
    target_name = "_freeconferencecall_session"

    for cookie in all_cookies:
        if cookie["name"] == target_name:
            # Удаляем, перезаписывая с пустым значением
            driver.delete_cookie(target_name)
            driver.refresh()

            # 5. Читаем и проверяем куку
            cookie = driver.get_cookie("_freeconferencecall_session")
            if cookie:
                print("✅ Кука '_freeconferencecall_session' успешно найдена:")
                print(f"   Значение: {cookie['name']}")
            else:
                print(" Кука '_freeconferencecall_session' не найдена.")

            print(f"Cookie '{target_name}' удалена.")
            break

finally:
    driver.quit()
