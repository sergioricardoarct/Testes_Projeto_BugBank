import time

from e2eTests.pages.RegistrarPage import RegistrarPage
from e2eTests.pages.LoginPage import LoginPage
from e2eTests.pages.HomePage import HomePage
import e2eTests.utils.Utils as Utils


class RegistrarTest:

    def test_registrar_usuario_com_dados_valido_e_sem_saldo(self, open_registrar):
        email, nome, senha = Utils.gerar_dados_registro()

        registrarPage = RegistrarPage(driver=open_registrar.driver)
        registrarPage.set_email(email)
        registrarPage.set_nome(nome)
        registrarPage.set_senha(senha)
        registrarPage.set_confirmar_senha(senha)
        registrarPage.click_btn_cadastrar()
        assert registrarPage.validar_conta_criada_sucesso()
        registrarPage.click_btn_fechar_modal()
        loginPage = LoginPage(driver=registrarPage.driver)
        loginPage.set_email(email)
        loginPage.set_password(senha)
        loginPage.click_button_acessar()
        homePage = HomePage(driver=loginPage.driver)
        assert homePage.validar_saldo_zerado()
        time.sleep(3)

