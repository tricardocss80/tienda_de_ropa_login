from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class PageLogin(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.intput_email = (By.ID, 'email')
        self.intput_password = (By.ID, 'passwd')
        self.button_sin_in = (By.XPATH, '//span[contains(.,"Sign in")]')
        self.block_error = (By.XPATH, '//p[contains(text(),"There is 1 error")]')
        self.the_error = (By.XPATH, '//div[@class="alert alert-danger"]//ol//li')
        self.driver = driver

    def login(self, data):
        self.wait_presence(self.intput_email).send_keys(data['email'])
        self.wait_presence(self.intput_password).send_keys(data['password'])

    def click_button_login(self):
        self.wait_clickable(self.button_sin_in).click()

    def error_container(self):
        return self.wait_presence(self.block_error).text

    def error(self):
        return self.wait_presence(self.the_error).text

