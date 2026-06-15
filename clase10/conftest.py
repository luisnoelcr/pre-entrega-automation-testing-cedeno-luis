import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Fixture que crea y cierra el navegador para cada test"""
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")
    servicio = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servicio, options=opciones)
    yield driver
    driver.quit()