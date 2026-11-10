import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

palabras = contenido.lower().split()
palabras_limpias = []
caracteres = ".,;:¿?¡!“”'\""

for palabra in palabras:
    elemento = palabra.strip(caracteres)
    palabras_limpias.append(elemento)

conteo = {}

for palabra in palabras_limpias:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

with open("estadisticas.txt", "w", encoding="utf-8") as salida:
    for palabra, cantidad in conteo.items():
        salida.write(f"{palabra}: {cantidad}\n")