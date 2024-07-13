from pages.modal_dialogs import ModalDialogs
import time


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.sidebar.visible()
    assert modal_dialogs.btns_in_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser) # обьект страницы
    modal_dialogs.visit() # вход на страницу
    browser.refresh() # обновление страницы браузера
    modal_dialogs.icon.click() # переход на главную страницу через иконку
    browser.back() # шаг назад в браузере
    browser.set_window_size(900, 400) # изменение размеров экрана
    time.sleep(2)
    browser.forward() # шаг вперед в браузере
    assert not modal_dialogs.equal_url() # проверка урла главной страницы
    assert browser.title == 'DEMOQA' # проверка тайтла на главной странице
    browser.set_window_size(1000, 1000) # возврат к размерам экрана
