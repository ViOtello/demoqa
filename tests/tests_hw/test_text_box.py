# 1. В папке домашних тестов создайте файл test_text_box.py, в нем реализуйте тест кейс
# a. перейти на страницу https://demoqa.com/text-box
# b. записать в поля Full Name, Current Address произвольный текст
# c. нажать на кнопку submit
# d. проверить, что снизу появились 2 элемента с нашим текстом
# i. * сравнение и ввод текста, реализовать через переменную
import time
from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    name: str = 'tester'
    address: str = 'sdfaksdfljasdb'

    text_box.visit()
    text_box.full_name.send_keys(name)
    text_box.current_address.send_keys(address)
    text_box.btn_submit.click_force()
    assert text_box.desk.visible()
    assert text_box.desk.check_count_elements(count=1)
    time.sleep(2)
    assert text_box.desk_name.get_text() == 'Name:' + name
    assert text_box.desk_current_address.get_text() == 'Current Address :' + address
