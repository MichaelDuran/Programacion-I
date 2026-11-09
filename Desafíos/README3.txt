Desafío 3: Administrador de contactos

Programa de consola en Python para administrar una lista de contactos: agregar, ver, buscar y eliminar.

Descripción

Cada contacto se guarda como un **diccionario** con tres datos: nombre, teléfono y correo electrónico.
Todos los contactos se almacenan en una **lista**, y las opciones del menú están en una **tupla**
porque no cambian durante la ejecución. Cada funcionalidad está implementada en su propia función.

Funcionalidades

1. Agregar un contacto nuevo (con validación de datos).
2. Ver la lista de contactos.
3. Buscar un contacto por nombre (sin distinguir mayúsculas y con coincidencia parcial).
4. Eliminar un contacto por nombre (con confirmación).
5. Salir del programa.

Cómo ejecutarlo

Requiere Python 3.

```bash
python Desafio_3.py
```

Estructura del código

| Función | Descripción |
|---|---|
| `telefono_valido()` | Valida que el teléfono tenga solo dígitos (con `+` opcional al inicio), de 7 a 15 dígitos. |
| `correo_valido()` | Valida que el correo tenga una sola `@`, texto antes de ella y un dominio con punto. |
| `pedir_dato()` | Repite la pregunta hasta que el dato sea válido; permite escribir `cancelar`. |
| `buscar_exacto()` | Devuelve el contacto con ese nombre exacto (sin importar mayúsculas), o `None`. |
| `formatear_contacto()` | Devuelve el texto con el que se muestra un contacto. |
| `mostrar_menu()` | Imprime el menú numerado. |
| `agregar_contacto()` | Pide y valida nombre, teléfono y correo, y guarda el contacto. |
| `ver_contactos()` | Muestra todos los contactos y cuántos hay. |
| `buscar_contacto()` | Busca por nombre y muestra las coincidencias. |
| `eliminar_contacto()` | Elimina un contacto por nombre, previa confirmación. |
| `menu_principal()` | Ciclo principal que muestra el menú y ejecuta la opción elegida. |

Conceptos de Python utilizados

- Listas, tuplas y diccionarios
- Funciones con parámetros y valores de retorno
- Ciclos `while` y `for`, y condicionales `if / elif / else`
- f-strings y `enumerate()`
- Métodos de texto: `.strip()`, `.lower()`, `.isdigit()`, `.split()`, `.startswith()`
- Lista por comprensión y funciones `lambda`
- Manejo de excepciones con `try / except`
- `if __name__ == "__main__":`

Robustez

- Nombre: no puede estar vacío (ni solo espacios) ni repetido.
- Teléfono: solo números, de 7 a 15 dígitos, con un `+` opcional al inicio.
- Correo: debe incluir una `@`, texto antes de ella, un dominio con punto y sin espacios.
- Si un dato es inválido, se vuelve a preguntar; se puede escribir `cancelar` para volver al menú sin guardar nada.
- Al ver, buscar o eliminar con la lista vacía, el programa avisa en lugar de pedir datos.
- Antes de eliminar se pide confirmación (`s`, `si` o `sí`); cualquier otra respuesta cancela.
- Las opciones de menú inválidas se manejan con un mensaje.
- `Ctrl+C` y `Ctrl+D` terminan el programa sin mostrar errores.

Limitaciones

- Los contactos se guardan solo en memoria: al cerrar el programa se pierden.
  Una mejora futura sería guardarlos en un archivo (`.txt` o `.json`).
- La validación del correo es básica: revisa el formato, no que el correo exista.
- Eliminar requiere el nombre exacto (sin importar mayúsculas), mientras que buscar acepta coincidencias parciales.

Ejemplo de uso

```
=== ADMINISTRADOR DE CONTACTOS ===
1. Agregar contacto
2. Ver contactos
3. Buscar contacto
4. Eliminar contacto
5. Salir
Escribe el número de la opción que quieres escoger: 1
(Escribe "cancelar" en cualquier momento para volver al menú)
Nombre: Ana
Teléfono (solo números, '+' opcional al inicio): +523312345678
Correo: ana@mail.com
Contacto agregado.

=== ADMINISTRADOR DE CONTACTOS ===
1. Agregar contacto
2. Ver contactos
3. Buscar contacto
4. Eliminar contacto
5. Salir
Escribe el número de la opción que quieres escoger: 2

Tienes 1 contacto(s):
Nombre: Ana | Teléfono: +523312345678 | Correo: ana@mail.com
```