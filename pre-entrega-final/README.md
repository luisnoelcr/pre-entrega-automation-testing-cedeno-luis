# Pre-Entrega Automation Testing — Cedeño Luis

## Propósito
Suite de pruebas automatizadas para verificar los flujos principales
de SauceDemo: login, navegación del catálogo e interacción con el carrito.

## Tecnologías utilizadas
- Python 3.14
- Selenium WebDriver 4.44
- Pytest 9.0
- pytest-html 4.2
- webdriver-manager 4.0

## Estructura del proyecto
pre-entrega-final/
├── tests/
│   ├── __init__.py
│   └── test_saucedemo.py   → suite principal de tests
├── utils/
│   ├── __init__.py
│   └── helpers.py          → funciones auxiliares reutilizables
├── reports/
│   └── reporte.html        → reporte HTML generado por Pytest
└── README.md

## Instalación de dependencias
pip install selenium webdriver-manager pytest pytest-html

## Cómo ejecutar las pruebas
cd pre-entrega-final
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html

## Casos de prueba
| Test | Descripción | Estado |
|---|---|---|
| test_login_exitoso | Login con credenciales válidas, valida URL y título | ✅ |
| test_inventario | Verifica título, cantidad de productos y primer item | ✅ |
| test_carrito | Agrega producto, verifica contador y listado en carrito | ✅ |
