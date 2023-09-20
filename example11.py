# Принимаем alert

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    input1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    input1.click()
    confirm = browser.switch_to.alert
    print(browser.switch_to.alert.text)
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()