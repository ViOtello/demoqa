from pages.accordian import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
import pytest
import time


def test_check_title_demo(browser):
    demo_qa_pages = DemoQa(browser)

    demo_qa_pages.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
# декоратор - который позволяет тестировать сразу несколько страниц
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'