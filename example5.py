# Проверка что кнопка недоступна после опред. кол-ва времени

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(11)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_button = button.get_attribute("disabled")
    print("Кнопка", button_button)


finally:
    time.sleep(7)
    browser.quit()