# tests/test_carrito.py

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_carrito_contiene_producto(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    inventario.agregar_primer_producto()
    carrito = inventario.ir_al_carrito()
    assert carrito.obtener_cantidad_items() == 1


def test_nombres_productos_en_carrito(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    inventario.agregar_primer_producto()
    carrito = inventario.ir_al_carrito()
    nombres = carrito.obtener_nombres_productos()
    assert len(nombres) > 0


def test_continuar_comprando_regresa_inventario(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    inventario.agregar_primer_producto()
    carrito = inventario.ir_al_carrito()
    inventario_regreso = carrito.continuar_comprando()
    assert "inventory" in driver.current_url