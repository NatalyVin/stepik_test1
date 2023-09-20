# Кликаем по checkboxes и radiobuttons
# Поиск сокровища с помощью get_attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(By.CSS_SELECTOR, "img ")
    x_element = element.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()

