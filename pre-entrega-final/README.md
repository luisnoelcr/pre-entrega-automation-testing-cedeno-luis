# Pre-Entrega - Automation Testing con Page Object Model

## Descripción
Suite de automatización de pruebas para SauceDemo usando Selenium + Pytest con patrón Page Object Model (POM).

## Estructura del proyecto

## Estructura del proyecto
pre-entrega-final/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
├── reports/
├── conftest.py
└── pytest.ini

## Ejecución

### Todos los tests
```bash
python -m pytest --html=reports/reporte_pom.html -v
```

### Solo smoke tests
```bash
python -m pytest -m smoke --html=reports/reporte_pom.html -v
```

## Resultados
9/9 tests pasando