
from selenium import webdriver

driver = webdriver.Chrome()
driver = webdriver.Chrome()


driver.close() # Закрытие одной вкладки, если их несколько
driver.quit() # Закрывает все окна браузера, в целом закрывает всю сессию

class Person:
    age = 23

person = Person()
print(getattr(person, 'age'))  # Выведет 23
setattr(person, 'age', 30)
print(person.age)  # Выведет 30

double = lambda x: x * 2
print(double(5))  # Выведет 10

enumerate(iterable, start=0)
