DESAFÍO 5: COMPOSICIÓN DE FUNCIONES

DESCRIPCIÓN DEL DESAFÍO
Crear una función llamada "componer" que reciba una lista de funciones y
retorne una nueva función que represente la composición de todas ellas.
La composición es una operación donde el resultado de una función se usa
como argumento de la siguiente.

Ejemplo:
    componer([f, g, h])(x)  equivale a  h(g(f(x)))


ARCHIVO
desafio_5.py


CÓMO EJECUTARLO
1. Abre el archivo desafio_5.py en VS Code.
2. Ejecútalo con el botón "Run Python File" o desde la terminal:

       python desafio_5.py

3. Se imprimirán en consola los resultados de 9 pruebas.


EXPLICACIÓN DE LA SOLUCIÓN
1. Validación de la entrada
   La función componer comprueba que el argumento sea una lista o tupla y
   que cada elemento sea una función (callable). Si no, lanza un TypeError
   con un mensaje descriptivo.

2. Closure
   componer define y retorna una función interna (funcion_compuesta) que
   "recuerda" la lista de funciones recibida, aun después de que componer
   haya terminado de ejecutarse.

3. Orden de aplicación
   La función compuesta aplica las funciones de izquierda a derecha:
   la primera recibe los argumentos originales y cada una de las demás
   recibe el resultado de la anterior.

4. *args y **kwargs
   La primera función de la lista puede recibir cualquier número de
   argumentos (posicionales o con nombre). Las siguientes reciben un solo
   valor: el resultado de la función previa.

5. Lista vacía
   Si la lista no contiene funciones, la función compuesta devuelve el
   valor recibido sin modificarlo (comportamiento de función identidad).


PRUEBAS INCLUIDAS
Prueba 1: Composición numérica -> ((3 + 1) * 2) ** 2 = 64
Prueba 2: Composición de textos -> "   hola mundo  " -> "¡HOLA MUNDO!"
Prueba 3: Uso de funciones lambda -> (8 - 5) * 10 = 30
Prueba 4: El orden importa -> (5 + 1) * 2 = 12  y  (5 * 2) + 1 = 11
Prueba 5: Composición con una sola función -> 11
Prueba 6: Lista vacía -> devuelve 99 sin cambios
Prueba 7: Primera función con varios argumentos -> (3 + 4) * 2 = 14
Prueba 8: Elemento que no es función -> TypeError esperado
Prueba 9: Argumento que no es lista ni tupla -> TypeError esperado


CONCEPTOS DE PYTHON UTILIZADOS
- Funciones de orden superior (funciones que reciben o retornan funciones)
- Closures
- *args y **kwargs
- Funciones lambda
- Validación de tipos con isinstance() y callable()
- Manejo de excepciones (try / except, raise)
- Docstrings y comentarios
- Bloque if __name__ == "__main__"