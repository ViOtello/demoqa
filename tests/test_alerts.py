import time
from pages.alerts import Alerts

def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert() # проверяем что алерта нет

    alert_page.alertButton.click() # нажимаем на кнопку по локатору
    time.sleep(2)
    assert alert_page.alert()  # проверяем что алерт появился


def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accept() # принимаем элемент и смотрим что нет активных элементов
    assert not alert_page.alert()


def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    alert_page.alert().dismiss() # нажимаем кнопку отмены
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'


def test_prompt(browser):
    alert_page = Alerts(browser)
    name = 'Vitaly'
    alert_page.visit()

    alert_page.promptButton.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept() # нажали кнопку окей
    assert alert_page.promptResult.get_text() == f'You entered { name }'


