Desafío 1: Palíndromos

Descripción del desafío
Un palíndrmo es una palabra o frase que se lee igual de adelante hacia atrás que de atrás hacia adelante, ignorando espacios,
puntuación y capitalización. El programa pide una cadena al usuario y determina si es un palíndromo.

Solución
El programa sigue estos pasos:

    1. Entrada: solicita al usuario una palabra o frase con input().
    2. Minúsculas: convierte el texto con .lower() para ignorar la capitalización.
    3. Limpieza: recorre el texto carácter por carácter con un ciclo for y, en cada vuelta:
        * Normaliza las vocales  