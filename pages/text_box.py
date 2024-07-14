from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)


        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.desk = WebElement(driver, '#output')
        self.desk_name = WebElement(driver, '#name')
        self.desk_current_address = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div['
                                                       '6]/div/p[2]', 'xpath')
        #получаем уникальный локатор xpath и указываем тип локатора