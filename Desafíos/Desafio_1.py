### Desafío 1
"""Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás que de atrás
hacia adelante, ignorando los espacios, puntuación y capitalización. El desafío es crear un
programa que tome una cadena ingresada por el usuario y determine si es un palíndromo"""

# Pedir al usuario una palabra o frase
phrase = input("Escribe tu frase o palabra: ")

# Convertir dicha frase/palabra en minúsculas
lower = phrase.lower()

# Diccionario: cada letra con tilde (llave) y su equivalente sin tilde (valor)
accents = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}

# Eliminar tildes, espacios y/o signos de puntuación
clean = ""
for letter in lower:
    letter = accents.get(letter, letter)  # si tiene tilde, la cambia; si no, la deja igual
    if letter.isalnum():
        clean += letter

# Escribir al revés la frase/palabra
clean_reverse = clean[::-1]

# Validación en caso de que se escriban sólo espacios y/o signos de puntuación
if clean == "":
    print("No escribiste letras ni números.")

# Si hay números y/o letras; comparar la frase/palabra con su contraparte al revés e imprimir un resultado
elif clean == clean_reverse:
    print("Tu frase/palabra es un palíndromo.")
else:
    print("Tu frase/palabra no es un palíndromo.")
    