from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class PageIndex(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_sin_in = (By.XPATH, '//a[@class="login"]')
        self.driver = driver

    def click_sin_in(self):
        self.wait_clickable(self.button_sin_in).click()
