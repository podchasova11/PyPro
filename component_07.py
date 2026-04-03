# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("https://demoqa.com/text-box")
# time.sleep(1)
#
# name_field = driver.find_element("xpath", "//input[@id='userName']")
# # print(name_field.is_enabled())
# time.sleep(1)
# assert name_field.get_attribute("value") == ""
# name_field.send_keys("Mila")
# name_field_value = name_field.get_attribute("value")
# assert "Mila" in name_field_value
#
# email_field = driver.find_element("xpath", "//input[@id='userEmail']")
# # Очищаем поле
# email_field.clear()
# # Проверяем, что в поле пусто
# assert email_field.get_attribute("value") == ""
# # Вводим новое значение в поле
# email_field.send_keys("podchasova11@yandex.ru")
# # Создаем переменную email_field_value и присваиваем ей значение
# email_field_value = email_field.get_attribute("value")
# # Проверяем что в поле User Email содержится введенный нами email "podchasova11@yandex.ru"
# assert "podchasova11@yandex.ru" in email_field_value
#
#
# current_address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
# # Очищаем поле
# current_address_field.clear()
# # Проверяем, что в поле пусто
# assert current_address_field.get_attribute("value") == ""
# # Вводим новое значение в поле
# current_address_field.send_keys("Moscow, Kirova str.")
# # Создаем переменную current_address_value и присваиваем ей значение "Moscow, Kirova str."
# current_address_value = current_address_field.get_attribute("value")
# # Проверяем что в поле содержится введенный нами current_address_value
# assert "Moscow, Kirova str." in current_address_value
#
#
# permanent_address_field = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
# # Очищаем поле
# permanent_address_field.clear()
# # Проверяем, что в поле пусто
# assert permanent_address_field.get_attribute("value") == ""
# # Вводим новое значение в поле
# permanent_address_field.send_keys("Canada, Ottawa")
# # Создаем переменную permanent_address_value и присваиваем ей значение
# permanent_address_value = permanent_address_field.get_attribute("value")
# # Проверяем что в поле содержится введенное значение
# assert "Canada, Ottawa" in permanent_address_value
#
#
# button_submit = driver.find_element("xpath", "//button[@id='submit']")
# time.sleep(1)
# assert button_submit.is_enabled() == True, "Button [Submit] is disabled"
# print(button_submit.is_enabled())


# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("https://the-internet.herokuapp.com/login")
# time.sleep(1)
#
# username_field = driver.find_element("xpath", "//input[@id='username']")
# time.sleep(1)
# assert username_field.get_attribute("value") == ""
# username_field.send_keys("tomsmith")
# username_field_value = username_field.get_attribute("value")
# assert "tomsmith" in username_field_value
#
# password_field = driver.find_element("xpath", "//input[@id='password']")
# # Очищаем поле
# password_field.clear()
# # Проверяем, что в поле пусто
# assert password_field.get_attribute("value") == ""
# # Вводим новое значение в поле
# password_field.send_keys("SuperSecretPassword!")
# # Создаем переменную email_field_value и присваиваем ей значение
# password_field_value = password_field.get_attribute("value")
# # Проверяем что в поле password содержится введенный password
# assert "SuperSecretPassword!" in password_field_value
#
# button_submit = driver.find_element("xpath", "//button[@class='radius']")
# time.sleep(1)
# assert button_submit.is_enabled() == True, "Button [Submit] is disabled"
# print(button_submit.is_enabled())
#
# button_submit.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSwitchToTargetException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # Ввод учётных данных
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")

    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.clear()
    password.send_keys("SuperSecretPassword!")

    # Клик по кнопке Login
    login_btn = wait.until(EC.element_to_be_clickable(("xpath", "//button[@class='radius']")))
    try:
        login_btn.click()
    except (InvalidSwitchToTargetException):
        print("Thrown when frame or window target to be switched doesn't exist")

    # Валидация успешного входа
    wait.until(EC.url_to_be("https://the-internet.herokuapp.com/secure"))
    assert "secure" in driver.current_url, "Не перешли на /secure"

    print("✅ Успешный вход подтверждён")

finally:
    driver.quit()







