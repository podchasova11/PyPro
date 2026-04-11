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
import time

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

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
#
# driver = webdriver.Chrome(options=options)
# try:
#     driver.get("https://www.freeconferencecall.com/login")
#
#     # 1. Удаляем конкретную cookie по имени:
#     # Сначала получаем текущие cookies,
#     all_cookies = driver.get_cookies()
#     target_name = "_freeconferencecall_session"
#
#     for cookie in all_cookies:
#         if cookie["name"] == target_name:
#             # Удаляем, перезаписывая с пустым значением
#             driver.delete_cookie(target_name)
#             driver.refresh()
#
#             # 5. Читаем и проверяем куку
#             cookie = driver.get_cookie("_freeconferencecall_session")
#             if cookie:
#                 print("✅ Кука '_freeconferencecall_session' успешно найдена:")
#                 print(f"   Значение: {cookie['name']}")
#             else:
#                 print(" Кука '_freeconferencecall_session' не найдена.")
#
#             print(f"Cookie '{target_name}' удалена.")
#             break
#
# finally:
#     driver.quit()
#
# #
# #
# import pickle
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# # 1. Настройка WebDriver (User-agent и скрытие автоматизации)
# options = Options()
# # options.add_argument("--disable-blink-features=AutomationControlled")
# # options.add_argument(
# #    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option("useAutomationExtension", False)
#
# service = Service()  # Укажите путь к драйверу, если он не в PATH
# driver = webdriver.Chrome(service=service, options=options)
#
# try:
#     # Шаг 1: Добавление товаров (имитация действий на сайте)
#     driver.get("https://tablepress.org/demo/")
#     print("Добавляем товары в корзину...")
#     # Здесь должен быть код кликов по кнопкам "Add to cart"
#     time.sleep(3)
#
#     # Шаг 2: Сохранение состояния (Cookies)
#     cookies = driver.get_cookies()
#     with open("session_cookies.pkl", "wb") as file:
#         pickle.dump(cookies, file)
#     print("Куки сохранены в файл.")
#
#     # Шаг 3: Очистка корзины (Удаление кук и перезагрузка)
#     driver.delete_all_cookies()
#     driver.refresh()
#     print("Корзина очищена (куки удалены), страница перезагружена.")
#     time.sleep(2)
#
#     # Шаг 4: Восстановление сессии
#     print("Восстанавливаем сессию из файла...")
#     with open("session_cookies.pkl", "rb") as file:
#         loaded_cookies = pickle.load(file)
#         for cookie in loaded_cookies:
#             driver.add_cookie(cookie)
#
#     driver.refresh()
#     print("Сессия восстановлена, корзина должна быть снова заполнена.")
#     time.sleep(5)
#
# finally:
#     driver.quit()


# //button[text()='Войти']

# //input[@name='login']
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
#
# driver = webdriver.Chrome(options=options)
# try:
#     driver.get("https://www.kufar.by/l")
#
#     # 5. Читаем и проверяем куку
#     cookie = driver.get_cookie("name")
#     if cookie:
#         print("✅ Кука 'name' успешно найдена:")
#         print(f"   Значение: {cookie['name']}")
#     else:
#         print(" Кука 'name' не найдена.")
#
#     break

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Настройка драйвера
# options = Options()
# driver = webdriver.Chrome(options=options)
#
# try:
#     # 1. Открываем сайт
#     driver.get("https://www.kufar.by/l")
#
#     # 2. Удаляем все существующие куки
#     driver.delete_cookie("session_id")()
#
#     # 3. Устанавливаем куку
#     driver.add_cookie({
#         "session_id": "mc1xac0d0aefea5d26362d676d466829a12abfa840f8",
#         "domain": ".kufar.by",  # важно: указать домен
#     })
#     time.sleep(22)
#     # 4. Обновляем страницу
#     driver.refresh()
#
#     # 5. Читаем и проверяем куку
#     cookie = driver.get_cookie("session_id")
#     if cookie:
#         print("✅ Кука 'session_id' успешно установлена:")
#         print(f"   Значение: {cookie['session_id']}")
#     else:
#         print(" Кука 'session_id' не найдена. Возможно, домен указаны неверно.")
#
#
#
# finally:
#     driver.quit()  # закрываем браузер



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Настройка драйвера
options = Options()
options.add_argument(
   "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

try:
    # 1. Открываем сайт — важно сначала посетить домен, иначе add_cookie не сработает
    driver.get("https://www.kufar.by/l")

    # 2. Удаляем конкретную по имени cookie)
    driver.delete_cookie("session_id")  # или driver.delete_all_cookies()
    driver.delete_cookie("kufar_cart_id")


    # 3. Устанавливаем куку
    driver.add_cookie({
        "name": "kufar_cart_id",
        "value": "mc1xac0d0aefea5d26362d676d466829a12abfa840f8",
        "domain": ".kufar.by"
    })

    driver.add_cookie({
        "name": "session_id",
        "value": "5826e8c6-1fcf-4586-9261-15c15e56ffb1",
        "domain": ".kufar.by"
    })

    # 4. Обновляем страницу, чтобы кука применилась
    driver.refresh()
    time.sleep(3)  # небольшой пауза для загрузки

    # 5. Проверяем
    cookie = driver.get_cookie("session_id")
    if cookie:
        print("✅ Кука 'session_id' успешно установлена:")
        print(f"   Значение: {cookie['value']}")
        print(f"   Домен: {cookie.get('domain', '—')}")
        print(f"   Secure: {cookie.get('secure', False)}")
    else:
        print("❌ Кука 'session_id' не найдена.")

    cookie = driver.get_cookie("kufar_cart_id")
    if cookie:
        print("✅ Кука 'kufar_cart_id' успешно установлена:")
        print(f"   Значение: {cookie['value']}")
        print(f"   Домен: {cookie.get('domain', '—')}")
        print(f"   Secure: {cookie.get('secure', False)}")
    else:
        print("❌ Кука 'kufar_cart_id' не найдена.")


finally:
    time.sleep(3)  # пауза для загрузки
    driver.quit()



