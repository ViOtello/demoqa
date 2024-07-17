from pages.webtables import WebTables
import time


def test_webtables(browser):
    webtables = WebTables(browser)
    webtables.visit()

    # проверка блока No rows found
    assert not webtables.no_data.exist()

    # удаляем все записи
    while webtables.btn_delete_row.exist():
        webtables.btn_delete_row.click()

    time.sleep(2)
    assert webtables.no_data.exist()

