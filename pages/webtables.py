from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, "[id*='delete-record-']", 'CSS')
        # [id*='delete-record-'] - поиск по частичному совпадению строки CSS

        self.btn_add = WebElement(driver, '#addNewRecordButton')  # кнопка эдд
        self.modal_backdrop = WebElement(driver, 'div.fade.modal.show')  # окно
        self.user_form = WebElement(driver, '#userForm')  # форма окна с отражением заполняемости
        self.btn_modal_submit = WebElement(driver, '#submit')  # кнопка сабмит в окне

        # заполнение окна
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.pencil = WebElement(driver, "[id*='edit-record-']")  # поиск по карандашу
        self.first_name_in_table = WebElement(driver,
                                 "//*[@id='app']/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[1]",
                                 'xpath')

        self.btn_next = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > '
                                           'div.web-tables-wrapper > div.ReactTable.-striped.-highlight > '
                                           'div.pagination-bottom > div > div.-next > button')
        self.btn_previous = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > '
                                               'div.web-tables-wrapper > div.ReactTable.-striped.-highlight > '
                                               'div.pagination-bottom > div > div.-previous > button')

        self.rows = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > '
                                       'div.ReactTable.-striped.-highlight > div.pagination-bottom > div > '
                                       'div.-center > span.select-wrap.-pageSizeOptions > select')
        self.btn_rows_5 = WebElement(driver, "//*[contains(text(), '5 rows')]", 'xpath')


        # заголовки столбцов таблицы
        self.st_first_name = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.st_last_name = WebElement(driver,
                                        '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]',
                                        'xpath')
        self.st_age = WebElement(driver,
                                        '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]',
                                        'xpath')
        self.st_email = WebElement(driver,
                                        '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[4]',
                                        'xpath')
        self.st_salary = WebElement(driver,
                                        '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[5]',
                                        'xpath')
        self.st_department = WebElement(driver,
                                        '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[6]',
                                        'xpath')
        self.st_action = WebElement(driver,
                                        '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[7]',
                                        'xpath')






