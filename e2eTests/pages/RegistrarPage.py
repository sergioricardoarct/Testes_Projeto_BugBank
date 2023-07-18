import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from e2eTests.pages.PageObject import PageObject
import e2eTests.locators.RegistrarLocators as RegistrarLocators


class RegistrarPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, email):
        self.driver.find_element(By.XPATH, RegistrarLocators.input_email_xpath).send_keys(email)

    def set_nome(self, nome):
        self.driver.find_element(By.XPATH, RegistrarLocators.input_nome_xpath).send_keys(nome)

    def set_senha(self, senha):
        self.driver.find_element(By.XPATH, RegistrarLocators.input_senha_xpath).send_keys(senha)

    def set_confirmar_senha(self, senha):
        self.driver.find_element(By.XPATH, RegistrarLocators.input_confirmar_senha_xpath).send_keys(senha)

    def click_toogle_conta_saldo(self):
        self.driver.find_element(By.ID, RegistrarLocators.toggle_conta_saldo_id).click()

    def click_btn_cadastrar(self):
        self.driver.find_element(By.XPATH, RegistrarLocators.btn_cadastrar_xpath).click()

    def click_btn_fechar_modal(self):
        self.driver.find_element(By.ID, RegistrarLocators.btn_fechar_modal_id).click()

    def validar_conta_criada_sucesso(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(ec.visibility_of_all_elements_located((By.ID, RegistrarLocators.txt_modal_id)))
        mensagem_sucesso = self.driver.find_element(By.ID, RegistrarLocators.txt_modal_id).text
        return "foi criada com sucesso" in mensagem_sucesso





