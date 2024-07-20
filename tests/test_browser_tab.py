import time
from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    page_browser = BrowserTab(browser)
    page_browser.visit()

    assert len(browser.window_handles) == 1 # проверка списка открытых вкладок
    page_browser.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0]) # переключаемся на первую вкладку
    time.sleep(2)
