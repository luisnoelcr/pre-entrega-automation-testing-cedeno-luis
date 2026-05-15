# Actividad 1 - Clase 7: Script de login en SauceDemo
# Verifica que el login con credenciales válidas redirige a /inventory.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    # Configuración del driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    try:
        # 1. Navegar a SauceDemo
        driver.get("https://www.saucedemo.com/")

        # 2. Ingresar credenciales (selectores de la clase 6)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Verificar URL
        url_actual = driver.current_url
        assert "/inventory.html" in url_actual, f"URL inesperada: {url_actual}"

        # RETO EXTRA: Verificar título de la página
        titulo = driver.find_element(By.CSS_SELECTOR, ".title").text
        assert titulo == "Products", f"Título inesperado: {titulo}"

        print("✅ Test OK - Login exitoso y título verificado")

    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")

    finally:
        driver.quit()

test_login()