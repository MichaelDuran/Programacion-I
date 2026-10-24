### Desafío 2
"""Crear un programa que tome una lista de números y genere un histograma basado en esos números
usando asteriscos para crear las barras del histograma."""

LIMITE_MAXIMO = 100

# Generador de histograma
while True:
    texto = input("Escribe los valores que quieres poner en el histograma: ")

# Las comas se cambian por espacios para que, por ejemplo "3,7,2" también funcione
    texto = texto.replace(",", " ")
    lista = texto.split()

# Si no hay nada que graficar (Enter solo o solo espacios)
    if len(lista) == 0:
        print("Por favor, escribe números para generar tu histograma.")
        continue # vuelve al inicio del while y pide la entrada otra vez

    numeros_enteros = []
    valido = True

    for numero in lista:
        try:
            n = int(numero)
        except ValueError:
            # Se activa con letras y también con números decimales
            print("Por favor, escribe sólo números enteros.")
            valido = False
            break # sale del for

        if n < 0:
            print("No se permiten números negativos.")
            valido = False
            break # sale del for

        if n > LIMITE_MAXIMO:
            print("El valor máximo permitido es " + str(LIMITE_MAXIMO) + ".")
            valido = False
            break

        numeros_enteros.append(n)

    if valido:
        break # sale del while: la entrada es correcta

# Dibuja el histograma
for n in numeros_enteros:
    print(str(n) + "|" + n * "*")