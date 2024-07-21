from pages.base_page import BasePage
from components.components import WebElement


class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.rad_yes = WebElement(driver, '#yesRadio')
        self.rad_imp = WebElement(driver, '#impressiveRadio')
        self.rad_no = WebElement(driver, '#noRadio')
        self.text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > p > span')

