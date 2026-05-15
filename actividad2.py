# Actividad 2 - Clase 7: Explorar el inventario de SauceDemo
# Verifica título, cantidad de productos y muestra nombre y precio del primero

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_inventario():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    try:
        # Login previo (necesario para acceder al inventario)
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 1. Verificar que el título sea "Products"
        titulo = driver.find_element(By.CSS_SELECTOR, ".title").text
        assert titulo == "Products", f"Título inesperado: {titulo}"
        print(f"✅ Título verificado: {titulo}")

        # 2. Verificar que haya al menos un producto en el inventario
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) >= 1, "No se encontraron productos en el inventario"
        print(f"✅ Productos encontrados: {len(productos)}")

        # 3. Mostrar nombre y precio del primer producto
        primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"✅ Primer producto: {primer_nombre} — {primer_precio}")

    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")

    finally:
        driver.quit()

test_inventario()