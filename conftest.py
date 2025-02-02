import pytest
from selenium import webdriver


@pytest.fixture(scope="session") #декоратор - функция изменяющая поведение другой функции
def browser():
    driver = webdriver.Chrome()
    yield driver # елд - чтобы элемент мог использоваться в функции
    #.set_window_size(1000, 1000)
    driver.quit()
