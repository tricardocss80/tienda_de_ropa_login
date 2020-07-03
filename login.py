#caso 1:
#1 - Ir a automationpractice                           0k
#2- Ir a login                                         0k
#3-poner una direccion de mail con formato erroneo     0k
#4-Poner un pass cualquiera                            0k
#5-Presionar el boton de login                         0k
#6-Verificar que se muestra el error de formato.       0k
#caso 2:
#1 - Ir a automationpractice                           0k
#2- Ir a login                                         0k
#3-poner una direccion de mail con formato correcto    0k
#4-Poner un pass cualquiera                            0k
#5-Presionar el boton de login                         0k
#6-Verificar que se muestra el error de autenticacion. 0k


import unittest
from selenium import webdriver
from pageindex import PageIndex
from pagelogin import PageLogin


class LoginCaseSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.IndexPage = PageIndex(self.driver)
        self.LoginPage = PageLogin(self.driver)

    def test001_login_checks(self):
        data = {
            'email': 'pepelopezgmail.com',
            'password': 'pepeba19'
        }
        self.IndexPage.click_sin_in()
        self.LoginPage.login(data)
        self.LoginPage.click_button_login()
        self.assertEqual(self.LoginPage.error_container(), 'There is 1 error')
        self.assertEqual(self.LoginPage.error(), 'Invalid email address.')
        self.LoginPage.close_browser()

    def test002_login_checks(self):
        data = {
            'email': 'pepe@lopezgmail.com',
            'password': 'pepeba19'
        }
        self.IndexPage.click_sin_in()
        self.LoginPage.login(data)
        self.LoginPage.click_button_login()
        self.assertEqual(self.LoginPage.error_container(), 'There is 1 error')
        self.assertEqual(self.LoginPage.error(), 'Authentication failed.')
        self.LoginPage.close_browser()


if __name__ == '__main__':
    unittest.main()