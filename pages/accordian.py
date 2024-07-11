from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.accordion_text_1 = WebElement(driver, '#section1Content > p')
        self.accordion_elem_1 = WebElement(driver, '#section1Heading')

        self.accordion_elem_2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.accordion_elem_3 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.accordion_elem_4 = WebElement(driver, '#section3Content > p')



