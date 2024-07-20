# # в файле test_check_modal.py автоматизируйте тест кейс
# a. страница https://demoqa.com/modal-dialogs
# i. на странице присутствуют 2 кнопки “Small modal” и “Large modal”
# ii. при клике на каждую открывается модальное окно
# iii. у каждого окна есть кнопка “close” по клику окно закрывается
# iv. *** Доработайте тестовый файл так, чтоб тест пропускался если страница недоступна.Подумайте, как можно проверять страницу на доступность.

import time
import pytest
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)

    modal_page.visit()
    time.sleep(2)

    assert not modal_page.alert()  # проверяем что алерта нет
    modal_page.btn_small_modal.click()  # нажимаем на кнопку по локатору
    assert modal_page.btn_close_small.exist()
    # assert modal_page.alert() # тут возникает ошибка, типо нет аллерта, хотя окно есть, т.к. кнопку клоуз на окне программа видит
    # def test_function():
    #     if not modal_page.alert():
    #         pytest.skip("unsupported configuration")
    # test_function() # код некорректен

    modal_page.btn_close_small.click() # нажимаем на кнопку закрытия окна
    assert not modal_page.alert()  # проверяем что алерта нет
    time.sleep(2)

    modal_page.btn_large_modal.click()  # нажимаем на кнопку по локатору
    assert modal_page.btn_close_large.exist()
    # test_function() # код некорректен
    modal_page.btn_close_large.click() # нажимаем на кнопку закрытия окна
    assert not modal_page.alert()  # проверяем что алерта нет