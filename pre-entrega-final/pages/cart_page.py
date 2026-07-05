# pages/cart_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_items(self):
        return self.driver.find_elements(*self._CART_ITEMS)

    def obtener_nombres_productos(self):
        elementos = self.driver.find_elements(*self._ITEM_NAMES)
        return [e.text for e in elementos]

    def obtener_cantidad_items(self):
        return len(self.obtener_items())

    def ir_a_checkout(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        return self

    def continuar_comprando(self):
        self.driver.find_element(*self._CONTINUE_SHOPPING).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)