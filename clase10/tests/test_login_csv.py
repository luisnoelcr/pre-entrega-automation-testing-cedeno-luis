import pytest
import pathlib
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

# Construimos la ruta al CSV relativa a este archivo
RUTA_CSV = pathlib.Path(__file__).parent.parent / 'datos' / 'login.csv'

# Cargamos los casos desde el CSV
CASOS_LOGIN = leer_csv_login(RUTA_CSV)


@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    """
    Test parametrizado que verifica el login con datos del CSV
    """
    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.enviar()

    if debe_funcionar:
        assert "inventory.html" in driver.current_url, \
            f"FALLO: {descripcion} debería ingresar al inventario"
    else:
        assert login.hay_error(), \
            f"FALLO: {descripcion} debería mostrar error"


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """
    Test de smoke para verificar que al menos un login funciona
    """
    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario("standard_user")
    login.completar_clave("secret_sauce")
    login.enviar()

    assert "inventory.html" in driver.current_url