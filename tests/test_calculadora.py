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

#-- FIXTURE FLOTANTES ------------------

@pytest.fixture
def numeros_flotantes():
    """Prepara un par de flotantes reutilizables en multiples tests."""
    return 0.1, 0.2


#-- TESTS MULTIPLICAR ------------------

@pytest.mark.smoke
def test_multiplicar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 100

@pytest.mark.smoke
def test_multiplicar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert multiplicar(a, b) == pytest.approx(0.02, rel=1e-4)


#-- PARAMETRIZACION RESTAR ------------------

@pytest.mark.smoke
@pytest.mark.parametrize("a, b, esperado", [
    (10, 3, 7),      # positivos
    (-5, -2, -3),    # negativos
    (0, 0, 0),       # caso limite
])
def test_restar_varios(a, b, esperado):
    assert restar(a, b) == esperado