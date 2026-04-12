import pytest
from calculadora import sumar, restar, multiplicar, dividir

#-- FIXTURE ------------------

@pytest.fixture
def numeros_enteros():
    """ Prepara un par de enteros reutilizables en multiples test"""
    return 20, 5

#-- TESTS CON FIXTURE --------------

@pytest.mark.smoke
def test_sumar_con_fixture(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) == 25


#-- PARAMETRIZACION -------------

@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),       # positivos
    (-1, -1, -2),    # negativos
    (2.5, 0.5, 3.0), # decimales
    (0, 0, 0),       # caso limite
])
def test_sumar_varios(a, b, esperado):
    assert sumar(a, b) == esperado


@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (7.5, 2.5, 3.0),
])
def test_dividir_varios(a, b, esperado):
    assert dividir(a, b) == pytest.approx(esperado, rel=1e-4)

#-- EXCEPCIONES --------------

@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError) as excinfo:
        dividir(1, 0)
    assert "cero" in str(excinfo.value).lower()

#-- ASERCIONES AVANZADAS -----------------------

@pytest.mark.smoke
def test_sumar_retorna_numero():
    resultado = sumar(3, 4)
    assert isinstance(resultado, (int, float))

@pytest.mark.smoke
def test_restar_basico():
    assert restar(10, 3) == 7
