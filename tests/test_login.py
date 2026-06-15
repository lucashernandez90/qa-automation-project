import pytest
from pages.login_page import LoginPage

USUARIO_VALIDO = "standard_user"
SENHA_VALIDA = "secret_sauce"

MSG_ERRO_LOGIN_INVALIDO = "Username and password do not match any user in this service"
MSG_ERRO_VAZIO = "Username is required"

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

def test_login_success(login_page):
    login_page.login(USUARIO_VALIDO, SENHA_VALIDA)
    assert login_page.is_logged()


def test_login_invalid_username(login_page):
    login_page.login("Lucas", SENHA_VALIDA)
    assert MSG_ERRO_LOGIN_INVALIDO in login_page.get_error_message()


def test_login_invalid_password(login_page):
    login_page.login(USUARIO_VALIDO, "senha_errada")
    assert MSG_ERRO_LOGIN_INVALIDO in login_page.get_error_message()


def test_login_empty_fields(login_page):
    login_page.login("", "")
    assert MSG_ERRO_VAZIO in login_page.get_error_message()