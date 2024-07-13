from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_qa_pages = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_pages.visit() # посещаем стр
    demo_qa_pages.btn_elements.click() # нажимаем на кнопку
    demo_qa_pages.refresh() # обновляем стр
    browser.refresh() # обновляем браузер
    browser.back() # переход на шаг назад
    browser.forward() # переход на шаг вперед
    assert elements_page.equal_url() # проверяем на соответствие урлу
