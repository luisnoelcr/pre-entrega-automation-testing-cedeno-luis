# utils/helpers.py
# Funciones auxiliares reutilizables para los tests de SauceDemo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def crear_driver():
    """
    Crea y retorna una instancia de ChromeDriver lista para usar.
    Usa WebDriverWait (espera explícita) en vez de implicitly_wait.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def login(driver, usuario="standard_user", password="secret_sauce"):
    """
    Realiza el login en SauceDemo con las credenciales recibidas.
    Usa espera explícita para garantizar que los elementos estén presentes.
    """
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(usuario)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()