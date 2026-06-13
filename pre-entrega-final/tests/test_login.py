# tests/test_login.py

import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


@pytest.mark.smoke
def test_login_usuario_invalido(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("usuario_falso", "clave_falsa")
    assert login.esta_error_visible()


def test_mensaje_error_credenciales_invalidas(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("locked_out_user", "secret_sauce")
    mensaje = login.obtener_mensaje_error()
    assert "Epic sadface" in mensaje