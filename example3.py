# Тест успешно проходит на странице http://suninjuly.github.io/registration1.htm
# Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
# Используемые селекторы должны быть уникальны (одинаковые для обоих страниц)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html" #"По умолчанию первый тест"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, 'first_block .first_class .first')
    input1.send_keys('Поехали')
    input2 = browser.find_element(By.CLASS_NAME, 'first_block .second_class .second')
    input2.send_keys("Ух бля")
    input3 = browser.find_element(By.CLASS_NAME, 'first_block .third_class .third')
    input3.send_keys("Приехали")
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(7)
    browser.quit()