
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from e2eTests.pages.PageObject import PageObject
import e2eTests.locators.HomeLocators as HomeLocators


class HomePage(PageObject):

    def __init__(self, driver):
        super().__init__(driver)

    def validar_saldo_zerado(self):
        saldo = self.driver.find_element(By.XPATH, HomeLocators.text_saldo_xpath).text
        saldo_float = float(saldo.replace('R$ ', '').replace(',', '.'))
        return saldo_float == 0





