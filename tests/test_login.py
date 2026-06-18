import pytest
from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

MSG_ERRO_LOGIN_INVALID = "Username and password do not match any user in this service"
EMPTY_MSG_ERRO = "Username is required"

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

def test_login_success(login_page):
    login_page.login(VALID_USER, VALID_PASSWORD)
    assert login_page.is_logged()


def test_login_invalid_username(login_page):
    login_page.login("Lucas", VALID_PASSWORD)
    assert MSG_ERRO_LOGIN_INVALID in login_page.get_error_message()


def test_login_invalid_password(login_page):
    login_page.login(VALID_USER, "senha_errada")
    assert MSG_ERRO_LOGIN_INVALID in login_page.get_error_message()


def test_login_empty_fields(login_page):
    login_page.login("", "")
    assert EMPTY_MSG_ERRO in login_page.get_error_message()