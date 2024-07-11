from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.accordian import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.accordion_text_1.visible()
    accordion_page.accordion_elem_1.click()
    time.sleep(2)
    assert not accordion_page.accordion_text_1.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.accordion_elem_2.visible()
    assert not accordion_page.accordion_elem_3.visible()
    assert not accordion_page.accordion_elem_4.visible()
