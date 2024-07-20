# 3. в файле test_sort.py автоматизируйте тест кейс:
# a. Страница https://demoqa.com/webtables
# b. при клике на каждый заголовок столбца страницы, происходит сортировка таблицы по этому столбцу
# (Для проверки сортировки, в данном кейсе, достаточно считывать соответствующий класс элемента)

from pages.webtables import WebTables
import time


def test_web_tables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    time.sleep(2)
    sort_a: str = '-sort-asc' # аттрибут класса сортировки по алфавиту от а до я
    sort_b: str = '-sort-desc' # аттрибут класса сортировки по алфавиту от я до а

    assert web_tables.st_first_name.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_first_name.click()
    assert web_tables.st_first_name.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_first_name.click()
    assert web_tables.st_first_name.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)

    assert web_tables.st_last_name.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_last_name.click()
    assert web_tables.st_last_name.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_last_name.click()
    assert web_tables.st_last_name.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)

    assert web_tables.st_age.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_age.click()
    assert web_tables.st_age.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_age.click()
    assert web_tables.st_age.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)

    assert web_tables.st_email.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_email.click()
    assert web_tables.st_email.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_email.click()
    assert web_tables.st_email.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)

    assert web_tables.st_last_name.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_last_name.click()
    assert web_tables.st_last_name.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_last_name.click()
    assert web_tables.st_last_name.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)

    assert web_tables.st_department.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_department.click()
    assert web_tables.st_department.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_department.click()
    assert web_tables.st_department.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)

    assert web_tables.st_action.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
    web_tables.st_action.click()
    assert web_tables.st_action.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_a} -cursor-pointer"
    web_tables.st_action.click()
    assert web_tables.st_action.get_dom_attribute('class') == f"rt-th rt-resizable-header {sort_b} -cursor-pointer"
    time.sleep(2)





