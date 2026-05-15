# tests/test_saucedemo.py
# Suite de pruebas automatizadas para SauceDemo
# Cubre: Login, Inventario y Carrito de compras

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Importar funciones auxiliares desde utils/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.helpers import crear_driver, login


# ─── FIXTURE ────────────────────────────────────────────────────────────────

@pytest.fixture
def driver():
    """
    Fixture de Pytest: crea el driver antes de cada test
    y lo cierra automáticamente al terminar.
    """
    driver = crear_driver()
    yield driver
    driver.quit()


# ─── TEST 1: LOGIN ───────────────────────────────────────────────────────────

def test_login_exitoso(driver):
    """
    Verifica que el login con credenciales válidas
    redirige a /inventory.html y muestra título 'Products'.
    """
    wait = WebDriverWait(driver, 10)

    login(driver)

    # Validar URL
    assert "/inventory.html" in driver.current_url, \
        f"URL inesperada: {driver.current_url}"

    # Validar título (criterio mínimo)
    titulo = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    ).text
    assert titulo == "Products", f"Título inesperado: {titulo}"


# ─── TEST 2: INVENTARIO ──────────────────────────────────────────────────────

def test_inventario(driver):
    """
    Verifica que el catálogo muestra título correcto,
    al menos un producto, y muestra nombre y precio del primero.
    """
    wait = WebDriverWait(driver, 10)

    login(driver)

    # Validar título
    titulo = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
    ).text
    assert titulo == "Products", f"Título inesperado: {titulo}"

    # Validar que haya al menos un producto
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) >= 1, "No se encontraron productos"

    # Mostrar nombre y precio del primero
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n→ Primer producto: {nombre} — {precio}")


# ─── TEST 3: CARRITO ─────────────────────────────────────────────────────────

def test_carrito(driver):
    """
    Agrega el primer producto al carrito, verifica el contador
    y comprueba que el producto aparece listado en el carrito.
    """
    wait = WebDriverWait(driver, 10)

    login(driver)

    # Agregar primer producto al carrito
    boton = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn_primary.btn_inventory")
        )
    )
    boton.click()

    # Verificar contador del carrito = 1
    contador = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text
    assert contador == "1", f"Contador inesperado: {contador}"

    # Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "/cart.html" in driver.current_url, \
        f"URL inesperada: {driver.current_url}"

    # Verificar producto en carrito
    items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(items) >= 1, "No hay productos en el carrito"
    nombre = items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"\n→ Producto en carrito: {nombre}")