def sumar(a, b):
    """Suma dos numeros y retorna el resultado"""
    return a + b

def restar(a, b):
    """Resta dos numeros y retorna el resultado"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos numeros y retorna el resultado"""
    return a * b

def dividir(a, b):
    """Divide dos numeros y retorna el resultado"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None

def calculadora():
    """Funcion principal de la calculadora"""
    print("=== CALCULADORA ===")

    try:
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
    except ValueError:
        print("Error: Debes ingresar numeros validos.")
        return

    print("Que operacion queres realizar?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elegi una opcion (1-4): ")

    if opcion == "1":
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == "2":
        print(f"Resultado: {restar(a, b)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == "4":
        print(f"Resultado: {dividir(a, b)}")
    else:
        print("Error: Opcion no valida.")

calculadora()