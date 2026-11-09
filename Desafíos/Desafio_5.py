# Desafío 5: Composición de funciones
# componer([f, g, h]) devuelve una nueva función que aplica f, luego g y luego h:
# resultado = h(g(f(x)))


def componer(funciones):
    """
    Recibe una lista (o tupla) de funciones y devuelve una nueva función
    que las aplica en orden, de izquierda a derecha.
    El resultado de cada función es el argumento de la siguiente.
    """
    # Validaciones (robustez)
    if not isinstance(funciones, (list, tuple)):
        raise TypeError("Se esperaba una lista o tupla de funciones.")

    for f in funciones:
        if not callable(f):
            raise TypeError(f"El elemento {f!r} no es una función (no es callable).")

    def funcion_compuesta(*args, **kwargs):
        # Si la lista está vacía, devolvemos el valor tal cual (función identidad)
        if not funciones:
            return args[0] if len(args) == 1 and not kwargs else args

        # La primera función puede recibir cualquier número de argumentos
        resultado = funciones[0](*args, **kwargs)

        # Las demás reciben el resultado de la anterior
        for f in funciones[1:]:
            resultado = f(resultado)

        return resultado

    return funcion_compuesta


# Funciones de ejemplo
def sumar_uno(x):
    return x + 1


def multiplicar_por_dos(x):
    return x * 2


def elevar_al_cuadrado(x):
    return x ** 2


def quitar_espacios(texto):
    return texto.strip()


def a_mayusculas(texto):
    return texto.upper()


def agregar_signos(texto):
    return f"¡{texto}!"


# Pruebas
if __name__ == "__main__":
    # Prueba 1: números -> ((3 + 1) * 2) ** 2 = 64
    f = componer([sumar_uno, multiplicar_por_dos, elevar_al_cuadrado])
    print("Prueba 1:", f(3))  # 64

    # Prueba 2: textos
    saludo = componer([quitar_espacios, a_mayusculas, agregar_signos])
    print("Prueba 2:", saludo("   hola mundo  "))  # ¡HOLA MUNDO!

    # Prueba 3: con funciones lambda
    g = componer([lambda x: x - 5, lambda x: x * 10])
    print("Prueba 3:", g(8))  # 30

    # Prueba 4: el orden importa
    a = componer([sumar_uno, multiplicar_por_dos])  # (x + 1) * 2
    b = componer([multiplicar_por_dos, sumar_uno])  # (x * 2) + 1
    print("Prueba 4:", a(5), b(5))  # 12 y 11

    # Prueba 5: una sola función
    print("Prueba 5:", componer([sumar_uno])(10))  # 11

    # Prueba 6: lista vacía (devuelve el valor sin cambios)
    print("Prueba 6:", componer([])(99))  # 99

    # Prueba 7: la primera función con varios argumentos
    h = componer([lambda a, b: a + b, multiplicar_por_dos])
    print("Prueba 7:", h(3, 4))  # 14

    # Prueba 8: manejo de errores
    try:
        componer([sumar_uno, "no soy una función"])
    except TypeError as e:
        print("Prueba 8 (error esperado):", e)

    try:
        componer(sumar_uno)
    except TypeError as e:
        print("Prueba 9 (error esperado):", e)