from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    _CARRITO_ICONO = (By.CLASS_NAME, "shopping_cart_link")
    _CARRITO_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def agregar_producto(self, nombre_producto):
        """Agrega un producto al carrito buscándolo por nombre"""
        productos = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item"
        )
        for producto in productos:
            nombre = producto.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text
            if nombre == nombre_producto:
                boton = producto.find_element(
                    By.CSS_SELECTOR, "button[class*='btn_primary']"
                )
                boton.click()
                return self
        raise ValueError(f"Producto '{nombre_producto}' no encontrado")

    def obtener_cantidad_carrito(self):
        """Retorna la cantidad de items en el carrito"""
        try:
            badge = self.wait.until(
                EC.visibility_of_element_located(self._CARRITO_BADGE)
            )
            return int(badge.text)
        except Exception:
            return 0