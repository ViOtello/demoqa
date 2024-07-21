from selenium.common.exceptions import NoSuchElementException
# импорт возможности исключений
from pages.base_page import BasePage
from components.components import WebElement
class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.podval_text = WebElement(driver, '#app > footer > span')

        self.h5 = WebElement(driver, "//*[@id='app']/div/div/div[2]/div/div", 'xpath')
        #self.h5 = WebElement(driver, '#app > div > div > div.home-body > div')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True

