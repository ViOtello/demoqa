from components.components import WebElement
from pages.base_page import BasePage

class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.polz = WebElement(driver, '//*[@id="sliderContainer"]/div[1]/span', 'xpath')
        self.text_pole =WebElement(driver, '//*[@id="sliderValue"]', 'xpath')

