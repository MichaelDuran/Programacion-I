Desafío 1: Palíndromos

Descripción del desafío
Un palíndrmo es una palabra o frase que se lee igual de adelante hacia atrás que de atrás hacia adelante, ignorando espacios,
puntuación y capitalización. El programa pide una cadena al usuario y determina si es un palíndromo.

Solución
El programa sigue estos pasos:

    1. Entrada: solicita al usuario una palabra o frase con input().
    2. Minúsculas: convierte el texto con .lower() para ignorar la capitalización.
    3. Limpieza: recorre el texto carácter por carácter con un ciclo for y, en cada vuelta:
        * Normaliza las vocales con tilde y dieresis (á, é. í, ó, ú, ü) a su versión sin tilde, usando un diccionario y el método
        .get(). La ñ se conserva, porque es una letra distinta de la n.
        * Conserva solo letras y números con .isalnum(), descartando espacios y signos de puntuación.
    4. Inversión: obtiene el texto limpio al revés con slicing ([::-1]).
    5. Validación y resultado: con if / elif / else se evalúan tres casos:
        * Si no quedó ningún carácter, avisa que no se escribieron letras ni números.
        * Si el texto limpio es igual a su inverso, es un palíndromo.
        * En cualquier otro caso, no es un palíndrmo.

Conceptos de Python utilizados
    * Entrada de datos con input()
    * Métodos de strings: .lower() y .isalnum()
    * Diccionarios y el método .get()
    * Ciclo for sobre una cadena
    * Concatenación de strings con +=
    * Slicing con paso negativo ([::-1])
    * Condicionales if / elif / else

Cómo ejecutarlo
python desafio_1.py

Ejemplos
Anita lava la tina = Tu frase/palabra es un palíndromo.
Hola = Tu frase/palabra no es un palíndromo.
!!! = No escribiste letras ni números.

Robustez
    * Texto sin letras ni números: si el usuario escribe solo espacios o signos de puntuación, el programa lo avisa. Sin esta
    validación, el texto vacío se compararía con su inverso y se reportaría incorrectamente como palíndromo.
    * Tildes: las vocales acentuadas se normalizan antes de comparar, por lo que no afectan el resultado.

Limitaciones conocidas
    * Solo se normalizan las vocales con tildes (á, é, í, ó, ú). Otros caracteres con diacríticos (por ejemplo: à, â) no se transforman.