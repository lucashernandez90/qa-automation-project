import pytest
from config.browser import create_driver

@pytest.fixture
def driver():

    driver = create_driver()
    yield driver #Envia o driver para o teste
    driver.quit()