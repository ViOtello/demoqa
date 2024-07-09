from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
def test_go_to_page_elements(browser):
    demo_qa_pages = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_pages.visit()
    assert demo_qa_pages.equal_url()
    demo_qa_pages.btn_elements.click()
    assert elements_page.equal_url()