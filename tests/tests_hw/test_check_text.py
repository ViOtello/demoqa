from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_1(browser) -> bool:
    demo_qa_pages = DemoQa(browser)

    demo_qa_pages.visit()
    if demo_qa_pages.podval.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        return True
    return False


def test_check_text_2(browser) -> bool:
    demo_qa_pages = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_pages.visit()
    demo_qa_pages.icon('#app > div > div > div.home-body > div > div:nth-child(1) > div > div.card-body').click()
    if demo_qa_pages.elem_text.get_text() == 'Please select an item from left to start practice.':
        return True
    return False
