from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_1(browser):
    demo_qa_pages = DemoQa(browser)
    demo_qa_pages.visit()
    assert demo_qa_pages.podval_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_2(browser):
    demo_qa_pages = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_pages.visit()
    demo_qa_pages.btn_elements.click()
    assert elements_page.elem_text.get_text() == 'Please select an item from left to start practice.'
