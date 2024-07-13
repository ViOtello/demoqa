from pages.demoqa import DemoQa


def test_check_title_demo(browser):
    demo_qa_pages = DemoQa(browser)

    demo_qa_pages.visit()
    assert browser.title == 'DEMOQA'
