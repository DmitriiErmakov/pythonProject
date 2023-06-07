import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.maximize_window()

def test_1(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_2(browser_open):
    browser.element('[name="q"]').should(be.blank).type('ldfjgljdfgjklfg').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу ldfjgljdfgjklfg ничего не найдено'))