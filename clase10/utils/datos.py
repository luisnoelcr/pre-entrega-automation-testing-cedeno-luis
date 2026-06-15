import csv
import json
import pathlib


def leer_csv_login(ruta_archivo):
    """
    Lee el archivo CSV de credenciales de login.
    Retorna lista de tuplas para pytest.mark.parametrize
    """
    datos = []
    ruta = pathlib.Path(ruta_archivo)
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            debe_funcionar = fila['debe_funcionar'].lower() == 'true'
            datos.append((
                fila['usuario'],
                fila['clave'],
                debe_funcionar,
                fila['descripcion']
            ))
    return datos


def leer_json_productos(ruta_archivo):
    """
    Lee el archivo JSON de productos.
    Retorna lista de nombres para parametrización
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        productos = json.load(archivo)
    nombres = [producto['nombre'] for producto in productos]
    return nombres


if __name__ == "__main__":
    casos = leer_csv_login('clase10/datos/login.csv')
    print("Casos CSV:", casos)

    productos = leer_json_productos('clase10/datos/productos.json')
    print("Productos JSON:", productos)