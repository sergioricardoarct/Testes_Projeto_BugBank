from datetime import time

from e2eTests.pages.HomePage import HomePage
from e2eTests.pages.LoginPage import LoginPage
from e2eTests.pages.RegistrarPage import RegistrarPage
from e2eTests.utils import Utils as Utils


class LoginTest:

    def test_efetuar_login_com_sucesso(self, open_login, open_registrar):
        print("Registar Usuário")
        email = 'aaaaa@gmail.com'
        nomeValido = "Aaaaa"
        senhaValida = "123123"

        registrarPage = RegistrarPage(driver=open_registrar.driver)
        registrarPage.set_email(email)
        registrarPage.set_nome(nomeValido)
        registrarPage.set_senha(senhaValida)
        registrarPage.set_confirmar_senha(senhaValida)
        registrarPage.click_btn_cadastrar()

        print("Logar Usuário")
        loginPage = LoginPage(driver=open_login.driver)
        loginPage.set_email(email)
        loginPage.set_password(senhaValida)
        loginPage.click_button_acessar()

        homePage = HomePage(driver=open_login.driver)
        assert homePage.validar_saldo_zerado()
        time(3)

    def test_login_sem_aroba(self, open_login):
        senha = Utils.gerar_senha()
        email_sem_arroba = "aaaaaa.gmail.com"

        loginPage = LoginPage(driver=open_login.driver)
        loginPage.set_email(email_sem_arroba)
        loginPage.set_password(senha)
        loginPage.click_button_acessar()

        assert loginPage.acesso_invalido()

    def test_login_sem_dot(self, open_login):
        senha = Utils.gerar_senha()
        email_sem_arroba = "aaaaaa@gmailcom"

        loginPage = LoginPage(driver=open_login.driver)
        loginPage.set_email(email_sem_arroba)
        loginPage.set_password(senha)
        loginPage.click_button_acessar()

        assert loginPage.acesso_invalido()

    def test_login_sem_email(self, open_login):
        senha = Utils.gerar_senha()

        loginPage = LoginPage(driver=open_login.driver)
        loginPage.set_password(senha)
        loginPage.click_button_acessar()

        assert loginPage.acesso_obrigatorio

    def test_login_email_sem_senha(self, open_login, open_registrar):
        print("Registar Usuário")
        email = 'aaaaa@gmail.com'
        nomeValido = "Aaaaa"
        senhaValida = "123123"

        registrarPage = RegistrarPage(driver=open_registrar.driver)
        registrarPage.set_email(email)
        registrarPage.set_nome(nomeValido)
        registrarPage.set_senha(senhaValida)
        registrarPage.set_confirmar_senha(senhaValida)
        registrarPage.click_btn_cadastrar()

        print("Logar Usuário")
        loginPage = LoginPage(driver=open_login.driver)
        loginPage.set_email(email)
        loginPage.click_button_acessar()

        assert loginPage.acesso_obrigatorio

    def test_login_nao_cadastrado(self, open_login, open_registrar):
        email = 'aaaaa@gmail.com'
        senhaValida = "123123"

        loginPage = LoginPage(driver=open_login.driver)
        loginPage.set_email(email)
        loginPage.set_password(senhaValida)
        loginPage.click_button_acessar()

        assert loginPage.senha_ou_email_invalido()
