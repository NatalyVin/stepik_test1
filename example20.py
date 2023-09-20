# Фикстуры (pytest)
# Cоздание и закрытие браузера для каждого теста во втором тест-сьюте
# @pytest.fixture - вынесено в отдельный файл conftest.py для постоянных фикстур (можно убрать данный блок)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture #(scope="class") - при добавлении данного значения тесты будут выполняться в одном браузере
                         #(autouse=True) - при добавлении данного значения фикстуру нужно запустить для каждого теста даже без явного вызова (т.е. можно не исп. переменную - будет запускаться апприори)
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()



class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")