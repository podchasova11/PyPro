from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Locator (improved: use By.XPATH instead of raw tuple)
VISIBLE_AFTER_BUTTON = ("xpath", "//div[@id='delayedText']")
DISAPPEARS_TEXT = ("xpath", "//div[@id='deletesuccess']")
CLICKABLE_BUTTON = ("xpath", "//input[@id='timerButton']")
TRY_IT_BUTTON = ("xpath", "//button[text()='Try it']")
MY_BUTTON = ("xpath", "//button[@id='myBtn']")


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # 'add_argument'

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)

try:
    driver.get("https://omayo.blogspot.com/")

    # Wait to become *invisiblity*
    wait.until(EC.invisibility_of_element_located(DISAPPEARS_TEXT))
    print("✅ Text invisiblity successfully.")

    # Wait for the button to become *visible* (not just present)
    wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))

    print("✅ Button [VISIBLE_AFTER_BUTTON] visible successfully.")

    # # Wait button to become *clickable*
    wait.until(EC.element_to_be_clickable(CLICKABLE_BUTTON))  # Ждем пока кнопка станет кликабельной (видимой + enabled)

    print("✅ Button [CLICKABLE_BUTTON] to become *clickable* successfully.")

    # # Wait button  [TRY_IT_BUTTON] to become *clickable*
    wait.until(EC.element_to_be_clickable(TRY_IT_BUTTON)).click()  # Ждем пока кнопка станет кликабельной (видимой + enabled)

    print("✅ Button [TRY_IT_BUTTON] to become *clickable* successfully.")

    # Ждем, пока атрибут 'disabled' элемента станет равным "true"
    wait.until(lambda driver: driver.find_element(*MY_BUTTON).get_attribute("disabled") == "true")

    print("✅ Button [MY_BUTTON] to become disabled")


finally:
    driver.quit()
