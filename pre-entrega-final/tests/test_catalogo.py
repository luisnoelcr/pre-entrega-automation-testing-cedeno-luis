# tests/test_catalogo.py

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_titulo_inventario(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    assert inventario.obtener_titulo() == "Products"


def test_productos_visibles(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    productos = inventario.obtener_productos()
    assert len(productos) > 0


def test_agregar_producto_al_carrito(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    inventario.agregar_primer_producto()
    assert inventario.obtener_contador_carrito() == 1