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

#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# # Настройка драйвера
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 30, poll_frequency=1)
#
# try:
#     driver.get("https://demoqa.com/dynamic-properties")
#
#     # Ожидаем, пока кнопка enableAfter станет кликабельной (видимой + enabled)
#     enable_after_button = wait.until(
#         EC.element_to_be_clickable((By.ID, "enableAfter"))
#     )
#     enable_after_button.click()
#
#     print("✅ Кнопка 'enableAfter' успешно найдена и кликнута.")
#
# finally:
#     # закрыть браузер
#     driver.quit()

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoAlertPresentException
#
# # --- Настройка драйвера (Chrome)
# # Убедитесь, что chromedriver в PATH или укажите путь:
# # driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 30)  # Явное ожидание до 30 секунд
#
# try:
#     # 1. Открыть сайт
#     driver.get("https://omayo.blogspot.com/")
#     print("[✓] Страница загружена")
#
#     # 2. Нажать кнопку 'Alert' и обработать алерт
#     alert_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Alert']")))
#     alert_btn.click()
#     print("[✓] Кнопка 'Alert' нажата")
#
#     # Ожидание алерта (до 10 сек — чтобы не ждать 30, если алерт появился быстро)
#     try:
#         alert = wait.until(EC.alert_is_present())
#         alert.accept()  # Программное подтверждение
#         print("[✓] Алерт успешно принят")
#     except TimeoutException:
#         print("[!] Алерт не появился в течение ожидания")
#
#     # 3. Выбрать 'Blue' из выпадающего списка
#     select_element = wait.until(EC.element_to_be_clickable((By.ID, "multiselect")))
#     select_element.click()
#
#     # Находим и кликаем по опции 'Blue'
#     blue_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Blue']")))
#     blue_option.click()
#     print("[✓] Выбрано значение 'Blue'")
#
#     # 4. Работа с iframe: переключиться и нажать 'Click me'
#     iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe1")))
#     click_me_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click me']")))
#     click_me_btn.click()
#     print("[✓] Кнопка 'Click me' внутри iframe нажата")
#
#     # Вернуться в основной контекст
#     driver.switch_to.default_content()
#
#     # Дополнительно: можно добавить проверку результата (например, текст после клика)
#     # Например: success_msg = wait.until(EC.visibility_of_element_located((By.ID, "result")))
#
# except TimeoutException as e:
#     print(f"[ERROR] Элемент не найден в течение 30 секунд: {e}")
# except Exception as e:
#     print(f"[ERROR] Неожиданная ошибка: {e}")
# finally:
#     # Опционально: раскомментируйте следующую строку, чтобы браузер не закрывался сразу
#     # input(\"Нажмите Enter для выхода...\")
#     driver.quit()
#     print("[ℹ] Драйвер закрыт")
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
# import logging
#
# # Настройка логирования
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# # Инициализация драйвера
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 30)  # Явное ожидание 30 сек
#
# try:
#     logger.info("Открываем страницу https://omayo.blogspot.com")
#     driver.get("https://omayo.blogspot.com")
#
#     # Список XPath и описаний кнопок
#     buttons = [
#         ("//*[@id=\"alert2\"]", "Кнопка 'Alert2'"),
#         ("//*[@id=\"delayedText\"]", "Кнопка 'Delayed Text'"),
#         ("//*[@id=\"timerButton\"]", "Кнопка 'Timer Button'"),
#         ("//*[@id=\"HTML44\"]//div[1]/button[2]", "Вторая кнопка в HTML44 (под заголовком 'Demo')"),
#     ]
#
#     for xpath, description in buttons:
#         try:
#             logger.info(f"Ищем: {description} по XPath → {xpath}")
#             element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#             element.click()
#             logger.info(f"✓ Успешно кликнули по: {description}")
#         except TimeoutException:
#             logger.error(f"✗ Не найден или не кликабелен: {description} (XPath: {xpath})")
#         except ElementClickInterceptedException:
#             logger.warning(f"⚠ Элемент видим, но перекрыт другим элементом: {description}. Попробуем прокрутку.")
#             try:
#                 driver.execute_script("arguments[0].scrollIntoView(true);", element)
#                 driver.implicitly_wait(1)
#                 element.click()
#                 logger.info(f"✓ Клик после прокрутки: {description}")
#             except Exception as e:
#                 logger.error(f"✗ Не удалось кликнуть даже после прокрутки: {description} — {e}")
#         except Exception as e:
#             logger.error(f"✗ Ошибка при работе с {description}: {e}")
#
# finally:
#     logger.info("Завершаем тест. Закрываем браузер.")
#     driver.quit()
#

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoAlertPresentException
# import logging
# import time
#
# # Настройка логирования
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# try:
#     # Инициализация драйвера
#     driver = webdriver.Chrome()
#     wait = WebDriverWait(driver, 30)  # Явное ожидание 30 сек
#     logger.info("Браузер запущен")
#
#     # Открытие страницы
#     driver.get("https://omayo.blogspot.com")
#     logger.info("Открыта страница https://omayo.blogspot.com")
#
#     # 1. Кнопка Alert
#     alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "alertb")))
#     alert_btn.click()
#     logger.info("Кнопка Alert нажата")
#
#     # Принятие алерта
#     try:
#         alert = wait.until(EC.alert_is_present())
#         alert.accept()
#         logger.info("Алерт принят")
#     except TimeoutException:
#         logger.warning("Алерт не появился в течение ожидания")
#
#     # 2. Выбор 'Blue' в мультивыборе — исправлено: прямой клик по <option>
#     select_element = wait.until(EC.presence_of_element_located((By.ID, "multiselect")))
#     driver.execute_script("arguments[0].scrollIntoView(true);", select_element)
#     time.sleep(0.5)
#
#     # Клик по option с текстом 'Blue'
#     blue_option = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//select[@id='multiselect']//option[text()='Blue']"))
#     )
#     blue_option.click()
#     logger.info("Опция 'Blue' выбрана напрямую через клик по <option>")
#
#     # 3. Переход в iframe и клик по кнопке 'Click me'
#     iframe = wait.until(EC.frame_to_be_available_and_switch_to_it("iframe1"))
#     click_me_btn = wait.until(EC.element_to_be_clickable((By.ID, "alertb")))
#     click_me_btn.click()
#     logger.info("Кнопка 'Click me' в iframe нажата")
#
#     # Возврат из iframe (опционально, но хорошая практика)
#     driver.switch_to.default_content()
#
# except Exception as e:
#     logger.error(f"Произошла ошибка: {e}")
# finally:
#     # Закрытие браузера
#     try:
#         driver.quit()
#         logger.info("Браузер закрыт")
#     except:
#         pass

#
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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")  # опционально, для фонового запуска
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.freeconferencecall.com/login")

    # Ждём, пока страница загрузится (хотя бы заголовок)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Удаляем куку строго для нужного домена
    # Сначала устанавливаем контекст домена — важно!
    driver.get("https://freeconferencecall.com")  # переход на базовый домен
    driver.delete_cookie("_freeconferencecall_session")

    # Возвращаемся на login и обновляем, чтобы убедиться
    driver.get("https://www.freeconferencecall.com/login")
    driver.refresh()

    # Ждём немного, даём JS время обработать
    wait.until(lambda d: True)  # минимальная пауза

    # Проверяем
    cookie = driver.get_cookie("_freeconferencecall_session")
    if cookie is None:
        print("✅ Кука '_freeconferencecall_session' успешно удалена — не найдена.")
    else:
        print(f"⚠️  Кука всё ещё присутствует:")
finally:
    driver.quit()