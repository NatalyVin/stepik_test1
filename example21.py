# Маркировка (запустить через командную страку pytest -s -v -m * example21.py) + метка зарегистированна в файле pytest.ini
# * - smoke, not smoke, smoke or regression
# @pytest.mark.skip - метка исп. для пропуска теста и не требует доп. регистрации
# @pytest.mark.xfail (reason = указать причину подения теста) - метка исп. чтоб пометить что кейс на исправлении (т.е. должен падать с ошибкой - будет помечен как xfailed),
                                                                                                   # после того как ошибка исправится будет помечен как xpassed

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print(23)

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print(24)