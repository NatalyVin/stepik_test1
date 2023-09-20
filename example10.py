# В форме регистрации требуется загрузить текстовый файл.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    elements = browser.find_elements(By.CSS_SELECTOR, ".form-control:required")
    for element in elements:
        element.send_keys("Мой ответ")

    input1 = browser.find_element(By.CSS_SELECTOR, "#file")
    input1.send_keys("C:/Users/ns.vinokurova/PycharmProjects/pythonProject1/myfile.txt")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(7)
    browser.quit()