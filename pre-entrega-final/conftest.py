# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado para todos los tests."""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        driver_path = ChromeDriverManager().install()
    except Exception as err:
        pytest.fail(
            f"No se pudo resolver el ChromeDriver via webdriver-manager: {err}. "
            "Verificar conectividad de red o instalación de Google Chrome."
        )

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()