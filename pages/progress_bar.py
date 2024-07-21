from components.components import WebElement
from pages.base_page import BasePage

class Progress(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)

        self.start_stop = WebElement(driver, '#startStopButton')
        self.text_pole = WebElement(driver, '#progressBar > div')

