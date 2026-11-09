# Desafío 4
"""Se crean nuestras propias versiones de las funciones map, filter y reduce. Estas funciones deben tomar como
argumentos una función y una lista (y un valor inicial en el caso de reduce) y deben retornar un iterable
(puedes retornar una lista)."""


"""Aplica `funcion` a cada elemento de `lista`.
Recibe: una función de un argumento y una lista.
Devuelve: una lista nueva con el resultado de cada aplicación."""

def mi_map(funcion, lista):
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado

"""Conserva solo los elementos de `lista` para los que `funcion` devuelve True.
Recibe: una función que devuelve True/False y una lista.
Devuelve: una lista nueva con los elementos que cumplen la condición."""

def mi_filter(funcion, lista):
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado

"""Acumula los elementos de `lista` en un solo valor usando `funcion`.
Recibe: una función de dos argumentos (acumulado, elemento), una lista y un valor inicial.
Devuelve: el valor acumulado final (si la lista está vacía, devuelve `inicial`)."""

def mi_reduce(funcion, lista, inicial):
    acumulado = inicial
    for elemento in lista:
        acumulado = funcion(acumulado, elemento)
    return acumulado

# Pruebas
def cuadrado(x):
    return x * x

def es_par(x):
    return x % 2 == 0

def sumar(a, b):
    return a + b

print(mi_map(cuadrado, [1, 2, 3]))             # [1, 4, 9]
print(mi_filter(es_par, [1, 2, 3, 4]))         # [2, 4]
print(mi_reduce(sumar, [1, 2, 3, 4], 0))       # 10
