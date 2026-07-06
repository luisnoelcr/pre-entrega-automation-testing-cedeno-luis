import pytest
import pathlib
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_json_productos

# Construimos la ruta al JSON relativa a este archivo
RUTA_JSON = pathlib.Path(__file__).parent.parent / 'datos' / 'productos.json'

# Cargamos los productos desde el JSON
PRODUCTOS = leer_json_productos(RUTA_JSON)


@pytest.fixture
def usuario_logueado(driver):
    """Fixture que realiza login antes de cada test de carrito"""
    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario("standard_user")
    login.completar_clave("secret_sauce")
    login.enviar()
    return driver


@pytest.mark.parametrize("producto", PRODUCTOS)
def test_agregar_producto_desde_json(usuario_logueado, producto):
    """Test que agrega cada producto del JSON al carrito"""
    inventario = InventoryPage(usuario_logueado)
    inventario.agregar_producto(producto)
    cantidad = inventario.obtener_cantidad_carrito()
    assert cantidad > 0, f"FALLO: El producto '{producto}' no se agregó al carrito"


@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    """Test de smoke que verifica funcionalidad básica del carrito"""
    inventario = InventoryPage(usuario_logueado)
    inventario.agregar_producto("Sauce Labs Backpack")
    cantidad = inventario.obtener_cantidad_carrito()
    assert cantidad == 1