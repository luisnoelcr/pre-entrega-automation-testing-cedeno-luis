# Actividad 2: Mostrar los primeros 10 numeros pares

print("Los primeros 10 numeros pares son:")

contador = 0
numero = 1

while contador < 10:
    if numero % 2 == 0:  # Verifica si el numero es par
        print(numero)
        contador += 1
    numero += 1  # Se incrementa en cada iteracion