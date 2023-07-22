import pytest

from e2eTests.pages.LoginPage import LoginPage
from e2eTests.pages.RegistrarPage import RegistrarPage


@pytest.fixture()
def open_login():
    print("Acessar página de login")
    login_page = LoginPage(browser='chrome')
    yield login_page
    print("Fechar página de login")
    login_page.close()


@pytest.fixture()
def login(open_login):
    print("Efetuar login")
    open_login.efetuar_login()
    yield open_login


@pytest.fixture()
def open_registrar(open_login):
    print("Abrir Registrar")
    open_login.click_button_registrar()
    yield open_login