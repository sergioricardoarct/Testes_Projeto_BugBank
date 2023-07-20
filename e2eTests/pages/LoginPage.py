from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import e2eTests.locators.LoginLocators as LoginLocators
from e2eTests.pages.PageObject import PageObject


class LoginPage(PageObject):
    # Métodos de SETUP
    base_url = 'https://bugbank.netlify.app/'

    def __init__(self, driver=None, browser='chrome'):
        super().__init__(driver, browser=browser)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.base_url)

    # Métodos SET
    def set_email(self, email):
        self.driver.find_element(By.XPATH, LoginLocators.input_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, LoginLocators.input_password_xpath).send_keys(password)

    # Clicks
    def click_button_registrar(self):
        self.driver.find_element(By.XPATH, LoginLocators.btn_registrar_xpath).click()

    def click_button_acessar(self):
        self.driver.find_element(By.XPATH, LoginLocators.btn_acessar_xpath).click()

    # Confirms

    def acesso_invalido(self):
        mensagem_invalida = self.driver.find_element(By.XPATH, LoginLocators.text_invalido_xpath).text

        return "Formato inválido" in mensagem_invalida

    def acesso_obrigatorio(self):
        wait = WebDriverWait(self.driver, 1)
        wait.until(ec.presence_of_element_located((By.XPATH, LoginLocators.text_obrigatorio_xpath)))
        mensagem_obrigatorio = self.driver.find_element(By.XPATH, LoginLocators.text_obrigatorio_xpath).text
        return "É campo obrigatório" in mensagem_obrigatorio

    def senha_ou_email_invalido(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(ec.visibility_of_all_elements_located((By.ID, LoginLocators.txt_modal_id)))
        mensagem_senha_ou_email_invaldio = self.driver.find_element(By.ID, LoginLocators.txt_modal_id).text
        return "Usuário ou senha inválido." in mensagem_senha_ou_email_invaldio
