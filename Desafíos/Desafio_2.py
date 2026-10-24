### Desafío 2
"""Crear un programa que tome una lista de números y genere un histograma basado en esos números
usando asteriscos para crear las barras del histograma."""

# Lista de números
lista = [3, 7, 2, 5, 1]

for numero in lista:
    print(str(numero) + "|" + numero * "*")