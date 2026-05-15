# Actividad 3 - Clase 7: Carrito rápido en SauceDemo
# Agrega el primer producto al carrito y verifica que esté listado

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_carrito():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    try:
        # Login previo
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 1. Clic en "Add to cart" del primer producto
        primer_boton = driver.find_elements(By.CSS_SELECTOR, ".btn_primary.btn_inventory")[0]
        primer_boton.click()
        print("✅ Producto agregado al carrito")

        # 2. Verificar que el contador del carrito muestre 1
        contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert contador == "1", f"Contador inesperado: {contador}"
        print(f"✅ Contador del carrito: {contador}")

        # 3. Navegar al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert "/cart.html" in driver.current_url, "No redirigió al carrito"
        print("✅ Navegación al carrito exitosa")

        # 4. Verificar que el producto está listado en el carrito
        items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items_carrito) >= 1, "No hay productos en el carrito"
        nombre_en_carrito = items_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"✅ Producto en carrito: {nombre_en_carrito}")

    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")

    finally:
        driver.quit()

test_carrito()