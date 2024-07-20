from pages.accordian import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
import pytest
import time


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
# декоратор - который позволяет тестировать сразу несколько страниц
def test_check_head_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'