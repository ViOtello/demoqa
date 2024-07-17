from components.components import WebElement
from pages.base_page import BasePage


class Koup(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.link_add = WebElement(driver, '/html/body/div[2]/div/ul/li[2]/a', 'xpath')
