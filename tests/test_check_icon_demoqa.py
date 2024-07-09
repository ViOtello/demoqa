from pages.demoqa import DemoQa


def test_check_icon(browser):
    demo_qa_pages = DemoQa(browser)
    demo_qa_pages.visit()
    demo_qa_pages.icon.click()
    assert demo_qa_pages.equal_url()
    demo_qa_pages.icon.exist()
