import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_open():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://google.com')


def test_search_selene(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_result(browser_open):
    browser.element('[name="q"]').should(be.blank).type('ldfjgljdfgjklfg').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу ldfjgljdfgjklfg ничего не найдено'))