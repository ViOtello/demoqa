from pages.demoqa import DemoQa
import time
import pytest


def test_decor_1(browser):
    page = DemoQa(browser)

    page.visit()
    assert page.h5.check_count_elements(6)

    for elem in page.h5.find_elements():
        assert elem.text != ''
@pytest.mark.skip
def test_decor_2(browser):
    page = DemoQa(browser)

    page.visit()
    assert page.h5.check_count_elements(6)

    for elem in page.h5.find_elements():
        assert elem.text != ''