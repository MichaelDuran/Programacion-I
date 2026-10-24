Desafío 2: Generador de Histograma

Descripción del desafío
Crear un programa que tome una lista de números y genere un histograma basado en esos números usando asteriscos
para crear las barras del histograma.

Cómo funciona la Solución
    1. El programa pide al usuario que escriba los valores con input().
    2. Las comas se reemplazan por espacios y el texto se separa con .split(), así que los números se puede separar
    con espacios o con comas.
    3. Cada valor se convierte a entero con int() y se valida.
    4. Por cada número se imprime una línea con el formato número|barra, donde la barra tiene tantos asteriscos como
    indica el número.

Conceptos de Python utilizados
input, .replace(), .split(), listas, ciclos for y while, try/except, condicionales, multiplicación de cadenas por enteros.

Cómo ejecutarlo
python desafio2_py

Formato de Entrada
    * Escribe números enteros separados por espacios o por comas. Ejemplos: 3 7 2 5 1 o 3, 7, 2, 5, 1
    * Se permiten valores entre 0 y 100
    * No uses decimales (ejemplo: 2.5), ni separadores de miles (ejemplo: 1,000): una coma se interpreta como separadores
    entre números, así que 1,000 se leería como 1 y 0, y 2,5 como 2 y 5.

Ejemplo
Entrada:
    Escribe los valores que quieres poner en el histograma: 3 7 2 5 1

Salida:
    3|***
    7|*******
    2|**
    5|*****
    1|*

Un 0 genera una barra vacía (0|)

Manejo de errores
Si la entrada no es válida, el programa muestra un mensaje y vuelve a pedir los números (no termina):

Entrada                                  | Mensaje
Enter sin escribir nada, o solo espacios | Por favor, escribe números para generar tu histograma.
Letras o decimales                       | Por favor, escribe sólo números enteros.
Números negativos                        | No se permite números negativos
Números mayores a 100                    | El valor máximo permitido es 100.

El límite 100 evita que un valor muy grande llene la terminal de asteriscos.

Decisiones de diseño
Decimales: se rechazan en lugar de redondearse, para no modificar en silencio los datos del usuario.
Cero: se permite, porque en un histograma representa una barra vacía.
Reintento: se usa un ciclo while para que el usuario pueda corregir su entrada sin reiniciar el programa.