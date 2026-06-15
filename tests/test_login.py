import pytest
from pages.login_page import LoginPage

# --- CONSTANTES PARA FACILITAR MANUTENÇÃO ---
USUARIO_VALIDO = "standard_user"
SENHA_VALIDA = "secret_sauce"

MSG_ERRO_USUARIO = "Username do not match"
MSG_ERRO_SENHA = "Password do not match"
MSG_ERRO_VAZIO = "Username and password are required"

@pytest.fixture
def login_page(driver):
    """Fixture que já entrega a página de login aberta e pronta para uso"""
    page = LoginPage(driver)
    page.open()
    return page

def test_login_success(login_page):
    login_page.login(USUARIO_VALIDO, SENHA_VALIDA)
    assert login_page.is_logged()


def test_login_invalid_username(login_page):
    login_page.login("Lucas", SENHA_VALIDA)
    assert MSG_ERRO_USUARIO in login_page.get_error_message()


def test_login_invalid_password(login_page):
    login_page.login(USUARIO_VALIDO, "senha_errada")
    assert MSG_ERRO_SENHA in login_page.get_error_message()


def test_login_empty_fields(login_page):
    login_page.login("", "")
    assert MSG_ERRO_VAZIO in login_page.get_error_message()