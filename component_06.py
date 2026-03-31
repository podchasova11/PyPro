from selenium import webdriver
import time

# Selenium Manager автоматически найдёт/скачает geckodriver
# Никаких дополнительных действий не требуется
driver = webdriver.Firefox()


# 1. Открываем VK
driver.get("https://vk.com")
print(f"VK title: '{driver.title}'")
time.sleep(1)

# 2. Переходим на Яндекс
driver.get("https://ya.ru")
print(f"Yandex title: '{driver.title}'")
time.sleep(1)

# 3. Возвращаемся назад (на VK)
driver.back()
time.sleep(1)
assert "VK" in driver.title or "ВКонтакте" in driver.title, f"Ожидали VK, но заголовок: '{driver.title}'"
print("✅ Вернулись на VK — assert пройден")

# 4. Обновляем страницу
driver.refresh()
time.sleep(1)

# 5. Выводим текущий URL
print(f"Текущий URL: {driver.current_url}")

# 6. Переходим вперёд (обратно на ya.ru)
driver.forward()
time.sleep(1)
assert "ya.ru" in driver.current_url.lower(), f"Ожидали ya.ru, но URL: '{driver.current_url}'"
print("✅ Перешли вперёд на ya.ru — assert пройден")


# Закрываем браузер
driver.quit()
print("\nБраузер закрыт.")
