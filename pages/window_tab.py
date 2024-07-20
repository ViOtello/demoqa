from pages.base_page import BasePage
from components.components import WebElement


class WindowTab(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)

        self.lnk_home = WebElement(driver, '#simpleLink')
