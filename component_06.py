
from selenium import webdriver

driver = webdriver.Chrome()
driver = webdriver.Chrome()


driver.close() # Закрытие одной вкладки, если их несколько
driver.quit() # Закрывает все окна браузера, в целом закрывает всю сессию
