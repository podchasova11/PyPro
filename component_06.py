import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://github.com/")
time.sleep(3)
elements = driver.find_elements(By.TAG_NAME, "h2")  # Находим все элементы h2
for element in elements:  # Перебираем список элементов
    print(element.text)  # Выводим текст элементов h2


driver.get("https://ya.ru/")
time.sleep(3)
elements = driver.find_elements(By.TAG_NAME, "h2")  # Находим все элементы h2
for element in elements:  # Перебираем список элементов
    print(element.text)  # Выводим текст элементов h2
driver.quit()

driver.close() # Закрытие одной вкладки, если их несколько
driver.quit() # Закрывает все окна браузера, в целом закрывает всю сессию
