# Desafio 3
"""Este programa permitirá administrar una lista de contactos. Cada contacto deberá tener un
nombre, un número de teléfono y una dirección de correo electrónico. El programa ofrece las
siguientes funcionalidades:
1. Agregar un contacto nuevo
2. Ver la lista de contactos
3. Buscar un contacto por nombre
4. Eliminar un contacto por nombre"""

contactos = []  # Lista de diccionarios
OPCIONES_MENU = ("Agregar contacto", "Ver contactos", "Buscar contacto", "Eliminar contacto", "Salir")


# ---------- Validaciones ----------

def telefono_valido(telefono):
    """Solo dígitos (0-9), con un '+' opcional al inicio. Entre 7 y 15 dígitos."""
    if telefono.startswith("+"):
        telefono = telefono[1:]
    return telefono.isdigit() and 7 <= len(telefono) <= 15


def correo_valido(correo):
    """Debe tener exactamente una '@', texto antes y un dominio con punto, sin espacios."""
    if "@" not in correo or " " in correo or correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    return (
        usuario != ""
        and "." in dominio
        and not dominio.startswith(".")
        and not dominio.endswith(".")
    )


# ---------- Funciones auxiliares ----------

def pedir_dato(mensaje, validar, mensaje_error):
    """Repite la pregunta hasta que el dato sea válido.
    Devuelve el dato limpio, o None si el usuario escribe 'cancelar'."""
    while True:
        dato = input(mensaje).strip()
        if dato.lower() == "cancelar":
            return None
        if validar(dato):
            return dato
        print(mensaje_error)


def buscar_exacto(nombre):
    """Devuelve el contacto cuyo nombre coincide exactamente (sin importar mayúsculas), o None."""
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return None


def formatear_contacto(contacto):
    return (f"Nombre: {contacto['nombre']} | "
            f"Teléfono: {contacto['telefono']} | "
            f"Correo: {contacto['correo']}")


# ---------- Funcionalidades ----------

def mostrar_menu():
    print("\n=== ADMINISTRADOR DE CONTACTOS ===")
    for i, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{i}. {opcion}")


def agregar_contacto():
    print('(Escribe "cancelar" en cualquier momento para volver al menú)')

    nombre = pedir_dato(
        "Nombre: ",
        lambda d: d != "" and buscar_exacto(d) is None,
        "El nombre no puede estar vacío ni estar repetido.",
    )
    if nombre is None:
        print("Operación cancelada.")
        return

    telefono = pedir_dato(
        "Teléfono (solo números, '+' opcional al inicio): ",
        telefono_valido,
        "Teléfono no válido. Solo números (con '+' opcional al inicio), de 7 a 15 dígitos.",
    )
    if telefono is None:
        print("Operación cancelada.")
        return

    correo = pedir_dato(
        "Correo: ",
        correo_valido,
        "Correo no válido. Debe incluir una '@'. Ejemplo: nombre@dominio.com",
    )
    if correo is None:
        print("Operación cancelada.")
        return

    contactos.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    print("Contacto agregado.")


def ver_contactos():
    if not contactos:
        print("No hay contactos.")
        return
    print(f"\nTienes {len(contactos)} contacto(s):")
    for contacto in contactos:
        print(formatear_contacto(contacto))


def buscar_contacto():
    if not contactos:
        print("No hay contactos.")
        return
    texto = input("Nombre a buscar: ").strip().lower()
    if not texto:
        print("Debes escribir un nombre.")
        return

    # Coincidencia parcial: "an" encuentra a "Ana" y a "Juan"
    resultados = [c for c in contactos if texto in c["nombre"].lower()]
    if not resultados:
        print("Contacto no encontrado.")
        return
    for contacto in resultados:
        print(formatear_contacto(contacto))


def eliminar_contacto():
    if not contactos:
        print("No hay contactos para eliminar.")
        return
    nombre = input("Nombre del contacto a eliminar: ").strip()
    if not nombre:
        print("Debes escribir un nombre.")
        return

    contacto = buscar_exacto(nombre)
    if contacto is None:
        print("Contacto no encontrado.")
        return

    confirmacion = input(f"¿Seguro que quieres eliminar a {contacto['nombre']}? (s/n): ").strip().lower()
    if confirmacion in ("s", "si", "sí"):
        contactos.remove(contacto)
        print("Contacto eliminado con éxito.")
    else:
        print("Eliminación cancelada.")


def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Escribe el número de la opción que quieres escoger: ").strip()
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Hasta la próxima.")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    try:
        menu_principal()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma terminado.")