from pages.radio import Radio
import time
import pytest

@pytest.mark.skipif(True, reason='just skip')
def test_decor_radio_1(browser):
    page = Radio(browser)

    page.visit()
    assert page.rad_yes.exist()
    assert page.rad_imp.exist()
    assert page.rad_no.exist()
    time.sleep(2)

    page.rad_yes.click_force()
    assert page.text.get_text() == 'Yes'

    page.rad_imp.click_force()
    assert page.text.get_text() == 'Impressive'

    assert 'dasabled' in page.rad_no.get_dom_attribute('class')
    # ошибка в написании условия
