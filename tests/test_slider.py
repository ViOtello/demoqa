import time
from selenium.webdriver import Keys
from pages.slider import Slider


def test_slider(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.polz.exist()
    assert slider.text_pole.exist()
    time.sleep(2)

    slider.polz.send_keys('50')
    slider.text_pole.send_keys('50')
    # поскольку эти значения интерактивны - гет дом аттрибут не подойдет

    # второе решение которое можно:
    while not slider.text_pole.get_dom_attribute('value') == '70':
        slider.polz.send_keys(Keys.ARROW_RIGHT)

    assert slider.text_pole.get_dom_attribute('value') == '70'
