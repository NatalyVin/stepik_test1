# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def sum(a, b):
  return a + b

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    a = a_element.text
    b = b_element.text
    c = sum(a, b)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()

