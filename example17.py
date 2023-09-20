#Запуск нескольких тестов через unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
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

        time.sleep(7)
        browser.quit()

    def test_abs2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
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

        time.sleep(7)
        browser.quit()

if __name__ == "__main__":
    unittest.main()