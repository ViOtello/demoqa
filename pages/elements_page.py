from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.elem_text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        # '#app > div > div > div.home-body > div > div:nth-child(1) > div > div.card-body'

        self.text_elements = WebElement(driver, 'div.col-12:nth-child(2)')

        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')

        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')