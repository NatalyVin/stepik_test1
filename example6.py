# Выбор любого числа из выпадающего списка

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1")
    #browser.find_element(By.TAG_NAME, "select").click()
    #browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()



finally:
    time.sleep(7)
    browser.quit()