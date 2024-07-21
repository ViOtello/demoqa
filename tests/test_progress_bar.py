import time
from selenium.webdriver import Keys
from pages.progress_bar import Progress


def test_progress_bar(browser):
    progress_bar = Progress(browser)

    progress_bar.visit()
    assert progress_bar.start_stop.exist()
    assert progress_bar.text_pole.exist()
    time.sleep(2)

    progress_bar.start_stop.click()

    while True: # пока тру будет выполняться
        if progress_bar.text_pole.get_dom_attribute('aria-valuenow') == '51':
            progress_bar.start_stop.click()
            break # остановить цикл

    time.sleep(2)


