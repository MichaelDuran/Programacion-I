"""ejercicio_1: Actividad de cadenas y persistencia (Etapas 1 a 4).

Convertido desde ejercicio_1.ipynb. El texto de las celdas Markdown se conserva
como comentarios. Las rutas parten de la carpeta de este archivo, que debe tener
la carpeta 'datos' a su lado (Unidad 3-4).
"""
from pathlib import Path

BASE = Path(__file__).resolve().parent


# ## Etapa 1
# ### DIÁGNOSTICO DE CADENAS

codigo = " mx-gdl-0042 "

#PRONÓSTICO len = 13
print(repr(len(codigo)))

#PRONÓSTICO codigo[2:4] = "x-"
print(repr(codigo[2:4]))

#PRONÓSTICO codigo[-6:-2] = "2400"
print(repr(codigo[-6:-2]))

#PRONÓSTICO codigo.strip() = "mx-gdl-0042"
print(repr(codigo.strip()))

#PRONÓSTICO codigo.upper() = " MX-GDL-0042 "
print(repr(codigo.upper()))

#PRONÓSTICO codigo.strip().upper() = "MX-GDL-0042"
print(repr(codigo.strip().upper()))

#PRONÓSTICO codigo.find("xyz") = -1
print(repr(codigo.find("xyz")))


# ### Diferencias entre el pronóstico y el resultado
# En cuanto a las operaciones con strings, sólo ha habido un pronóstico el cual fue erróneo.
# codigo[-6:-2]. He tenido una confusión a la hora de leer los índices negativos. Este error me ha hecho prestar más atención sobre este tipo de índices y he aprendido a usarlo de manera correcta.
#
# ### ¿codigo.strip() modifica si no se reasigna?
# No, ya que una operación no modifica la cadena original. Produce una nueva cadena que debe asignarse o utilizarse.
#
# ### ¿Qué diferencia existe entre in y find()?
# in te arroja un resultado booleano (TRUE/FALSE) en donde te menciona si un elemetno está presente dentro de una secuencia nombrada. En cuanto a find(), te encuentra en qué índice está localizada la primer coincidencia de la substring buscada.
#
# ### ¿Por qué un resultado -1 no debe utilizarse como posición encontrada?
# Porque el -1 significa que dentro de la secuencia nombrada no se ha encontrado la substring buscada.


# ### Leer etiquetas.txt
# Cuenten categorías distintas antes de limpiar, eliminando únicamente el salto de línea. Luego normalicen y vuelvan a contar. Propongan un caso en el que capitalize() alteraría una sigla que debe conservarse.

with open(BASE / "datos" / "etiquetas.txt", "r", encoding="utf-8") as f:
    etiquetas_crudas = [linea.rstrip("\n") for linea in f]

print("\n".join(etiquetas_crudas)) #original
print() #linea en blanco

categorias_crudas = len(etiquetas_crudas)
print("Hay", categorias_crudas, "categorias distintas antes de normalizar") #obtendremos el número de categorías

etiquetas_normalizadas = set([e.replace("-", " ").replace("_", " ").strip().capitalize() for e in etiquetas_crudas])

print("\n".join(etiquetas_normalizadas))
print() #linea en blanco

categorias_unicas_normalizadas = len(etiquetas_normalizadas)
print("Ahora hay", categorias_unicas_normalizadas, "categorias diferentes")


# ### Caso en el que capitalize() alteraria una sigla que debe conservarse
# Debido a que capitalize() hace que nuestros datos pone en minuscula todos los caracteres, excepto el primero; nuestros datos pueden perder forma cuando tengamos valores cuyas siglas deban permanecer en mayúsculas, como por ejemplo:
# - Codigo QR
# - Soporte VPN
# - IMSS/ISSSTE
#
# Si usamos capitalize() nuestros valores serán cambiados a:
# - Codigo qr
# - Soporte vpn
# - Imss/issste


# ## Contrato de datos y reglas de validacion
# solicitudes.txt contiene una cabecera y 30 líneas de datos, incluida una línea vacía. Cada registro usa cuatro campos separados por |. En este archivo no aparecen separadores ni saltos de línea dentro de los campos; por eso puede utilizarse split("|").

with open(BASE / "datos" / "solicitudes.txt", "r", encoding="utf-8") as g:
   solicitudes_crudas = [linea.rstrip("\n") for linea in g]
   
print("\n".join(solicitudes_crudas)) #original
print() #linea en blanco
   
print("Hay", len(solicitudes_crudas) -1, "solicitudes.")


# La cabecera ocupa la línea 1. Se numera con enumerate(archivo, start=2)

with open(BASE / "datos" / "solicitudes.txt", "r", encoding="utf-8") as g:
    encabezado = next(g).rstrip("\n")
    for n, linea in enumerate(g, start=2):   # la cabecera es la línea 1
        linea = linea.rstrip("\n")           # texto original, sin filtrar


# Se evalua cada linea en este orden: id, correo, categoria, descripcion.

def normalizar_id(i):
    return i.strip().upper()

def normalizar_correo(c):
    return c.strip().lower()

def normalizar_categoria(c):
    c = c.strip().lower().replace("-", " ").replace("_", " ")
    return "_".join(c.split())

def normalizar_descripcion(d):
    return " ".join(d.split())

"""Probar si funciona nuestro normalizadores"""
print(normalizar_id(" sol-0001 "))                   # SOL-0001
print(normalizar_correo(" Alumno1@CUCEA.udg.mx "))   # alumno1@cucea.udg.mx
print(normalizar_categoria(" PAGO_EN_LÍNEA "))       # pago_en_línea
print(normalizar_descripcion("  No puedo   entrar ")) # No puedo entrar

CATALOGO = {"acceso", "pago_en_línea", "soporte_técnico"}
DIGITOS = "0123456789"

def id_valido(i):
    return len(i) == 8 and i[:4] == "SOL-" and all(c in DIGITOS for c in i[4:])

def correo_valido(c):
    if c.count("@") != 1 or " " in c:
        return False
    local, dominio = c.split("@")
    return bool(local) and bool(dominio) and "." in dominio[1:-1]

def evaluar(linea, vistos):
    if linea.strip() == "":
        return None, "línea vacía"
    campos = linea.split("|")
    if len(campos) != 4:
        return None, "cantidad de campos distinta de cuatro"
    if "" in [c.strip() for c in campos]:
        return None, "campo vacío"
    id_, correo, categoria, descripcion = campos
    id_ = normalizar_id(id_)
    correo = normalizar_correo(correo)
    categoria = normalizar_categoria(categoria)
    descripcion = normalizar_descripcion(descripcion)
    if not id_valido(id_):
        return None, "ID con formato inválido"
    if not correo_valido(correo):
        return None, "correo inválido"
    if categoria not in CATALOGO:
        return None, "categoría fuera del catálogo"
    if id_ in vistos:
        return None, "ID duplicado"
    return [id_, correo, categoria, descripcion], None


# Las solicitudes rechazadas aparecerán con su número de línea, el motivo por el cual fue rechazada y el texto original de la solicitud.

validos = []
rechazos = []
vistos = set()

with open(BASE / "datos" / "solicitudes.txt", "r", encoding="utf-8") as g:
    encabezado = next(g).rstrip("\n")
    for n, linea in enumerate(g, start=2):
        linea = linea.rstrip("\n")
        registro, motivo = evaluar(linea, vistos)
        if motivo:
            rechazos.append((n, motivo, linea))
        else:
            vistos.add(registro[0])
            validos.append(registro)

print("Válidos:", len(validos))
print("Rechazados:", len(rechazos))
for r in rechazos:
    print(r)


# Dentro de nuestras solicitudes, 24 han sido validadas con los requisítos para que sean aceptados y 6 han sido rechazadas según si es una línea o campo vacía, se ha registrado un correo o ID con formato inválido, si ha habido una cantidad de campos distinta a cuatro o si el ID ha sido duplicado.

"""Se agrega un ID al conjunto de vistos únicamente cuando se acepte el registro completo"""
print(repr(vistos))


# ## ETAPA 2
# ### Ejemplo guiado
# Revisen ejemplo_guiado.py y ejecútenlo dos veces. Expliquen por qué errores.txt conserva dos líneas y ejecuciones.log aumenta. Identifiquen dónde se usa strip(), split(), replace(), capitalize(), una f-string y el cierre automático de archivos.
#
# ### ¿Por qué errores.txt conserva dos líneas?
# En la línea 12, errores.txt se abre con modo "w".
# with (SALIDA / "errores.txt").open("w", encoding="utf-8") as salida:
#
# El modo "w" vacía el archivo cada vez que se abre y lo escribe desde cero. En cada ejecución el script vuelve a leer eventos.txt, encuentra las mismas dos líneas con " ERROR " y las escribe de nuevo sobre un archivo recién vaciado. Por eso el resultado siempre es el mismo (dos líneas), sin importar cuántas veces se ejecute.
#
# ### ¿Por qué ejecuciones.log aumenta?
# En la línea 18 se abre con modo "a".
# with (SALIDA / "ejecuciones.log").open("a", encoding="utf-8") as historial:
#     historial.write(f"Errores detectados: {total}\n")
#
# El modo "a" conserva lo que ya había y agrega uno al final. Cada ejecución suma una línea nueva.
#
# Nota: "w" sirve para resultados que se regeneran y "a" para historiales.
#
# ### Dónde se usa cada cosa
# | Elemento | Línea | Código |
# |---|---|---|
# | strip() | 7 | etiqueta.strip() #quita los espacios de los extremos |
# | split() | 7 | .split(":") #separa en nombre y valor |
# | replace() | 8 | nombre.replace("_", " ") #cambia el guion bajo por espacio |
# | capitalize() | 8 | .capitalize() #deja "sensor norte" como "Sensor norte" |
# | f-string | 9, 19, 20, 22 | #ejemplo: f"Valor: {float(valor):.1f}" |
# | cierre automático de archivos | 11, 12, 18 | los tres with |


# ## Etapa 3 y etapa 4
# ### Implementación del depurador, persistencia y verificación

"""Completa los TODO conforme a las reglas del documento Word."""
from pathlib import Path
from datetime import datetime
import json
import sys
BASE = Path(__file__).resolve().parent
ENTRADA = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "datos" / "solicitudes.txt"
SALIDA = Path(sys.argv[2]) if len(sys.argv) > 2 else BASE / "salidas"
ENCABEZADO_ESPERADO = "id|correo|categoria|descripcion"
CATALOGO = {"acceso", "pago_en_línea", "soporte_técnico"}
DIGITOS = "0123456789"

class EncabezadoInvalido(Exception):
    """La primera línea del archivo no coincide con el encabezado esperado."""

def normalizar_categoria(texto):
    """Entrada: str. Salida: str en minúsculas unidas por _"""
    texto = texto.strip().lower().replace("-", " ").replace("_", " ")
    return "_".join(texto.split())

def id_valido(i):
    """Entrada: str. Salida: True si es SOL- y cuatro dígitos ASCII."""
    return len(i) == 8 and i[:4] == "SOL-" and all(c in DIGITOS for c in i[4:])

def correo_valido(c):
    """Entrada: str. Salida: True si cumple la validación didáctica"""
    if c.count("@") != 1 or " " in c:
        return False
    local, dominio = c.split("@")
    return bool(local) and bool(dominio) and "." in dominio[1:-1]

def validar_campos(campos, ids_vistos):
    """Entrada: lista de 4 campos sin normalizar y conjunto de IDs aceptados.
    Salida: (registro_limpio, None) si es válido o (None, motivo) si no lo es."""
    campos = [c.strip() for c in campos]
    if "" in campos:
        return None, "campo vacío"
    id_, correo, categoria, descripcion = campos
    id_ = id_.upper()
    correo = correo.lower()
    categoria = normalizar_categoria(categoria)
    descripcion = " ".join(descripcion.split())
    if not id_valido(id_):
        return None, "ID con formato inválido"
    if not correo_valido(correo):
        return None, "correo inválido"
    if categoria not in CATALOGO:
        return None, "categoría fuera del catálogo"
    if id_ in ids_vistos:
        return None, "ID duplicado"
    return [id_, correo, categoria, descripcion], None

def procesar(ruta):
    """Lee la entrada por líneas. Devuelve (validos, rechazos, por_categoria, vacias)."""
    validos, rechazos, ids_vistos, por_categoria = [], [], set(), {}
    vacias = 0
    total = 0
    with ruta.open("r", encoding="utf-8") as entrada:
        encabezado = next(entrada).rstrip("\n")
        if encabezado != ENCABEZADO_ESPERADO:
            raise EncabezadoInvalido(f"Encabezado inesperado: {encabezado!r}")
        for n, linea in enumerate(entrada, start=2):
            linea = linea.rstrip("\n")
            total += 1
            if linea.strip() == "":
                vacias +=1
                registro, motivo = None, "línea vacía"
            else:
                campos = linea.split("|")
                if len(campos) != 4:
                    registro, motivo = None, "cantidad de campos distinta de cuatro"
                else:
                    registro, motivo = validar_campos(campos, ids_vistos)
            if motivo:
                rechazos.append({"linea": n, "motivo": motivo, "texto_original": linea})
            else:
                ids_vistos.add(registro[0])
                validos.append(registro)
                por_categoria[registro[2]] = por_categoria.get(registro[2], 0) + 1
    return validos, rechazos, por_categoria, vacias, total

def escribir_limpias(validos):
    """Entrada: lista de registros. Escribe solicitudes_limpias.txt (modo w)."""
    with (SALIDA / "solicitudes_limpias.txt").open("w", encoding="utf-8") as f:
        f.write(ENCABEZADO_ESPERADO + "\n")
        for registro in validos:
            f.write("|".join(registro) + "\n")

def escribir_rechazos(rechazos):
    """Entrada: lista de dicts. Escribe rechazos.jsonl (modo w), un JSON por línea."""
    with (SALIDA / "rechazos.jsonl").open("w", encoding="utf-8") as f:
        for rechazo in rechazos:
            f.write(json.dumps(rechazo, ensure_ascii=False) + "\n")

def escribir_resumen(total, validos, rechazados, por_categoria):
    """Escribe resumen.json (modo w) con los conteos de esta ejecución."""
    resumen = {
        "total": total,
        "validos": validos,
        "rechazados": rechazados,
        "por_categoria": por_categoria,
    }
    with (SALIDA / "resumen.json").open("w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)

def registrar_ejecucion(total, validos, rechazados):
    """Agrega una línea a ejecuciones.log (modo a)."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with (SALIDA / "ejecuciones.log").open("a", encoding="utf-8") as f:
        f.write(f"{ahora} | {ENTRADA.name} | total={total} validos={validos} rechazados={rechazados}\n")

def verificar(total, validos, rechazados, por_categoria):
    """Reabre las salidas y compara lo persistido con los contadores."""
    with (SALIDA / "solicitudes_limpias.txt").open("r", encoding="utf-8") as f:
        next(f)         #excluir cabecera
        limpias = sum(1 for _ in f)
    with (SALIDA / "resumen.json").open("r", encoding="utf-8") as f:
        resumen = json.load(f)
    with (SALIDA / "rechazos.jsonl").open("r", encoding="utf-8") as f:
        lineas_rechazo = [json.loads(linea) for linea in f]
        assert limpias == validos, f"limpias={limpias} != validos={validos}"
        assert len(lineas_rechazo) == rechazados, "rechazos.jsonl no coincide"
        assert resumen["total"] == total, "resumen.total no coincide"
        assert resumen["validos"] == validos, "resumen.validos no coincide"
        assert resumen["rechazados"] == rechazados, "resumen.rechazados no coincide"
        assert resumen["por_categoria"] == por_categoria, "resumen.por_categoria no coincide"
        assert total == validos + rechazados, "total != validos + rechazados"
        assert sum(resumen["por_categoria"].values()) == validos, "suma por categoria != validos"

def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    try:
        validos, rechazos, por_categoria, vacias, total = procesar(ENTRADA)
        escribir_limpias(validos)
        escribir_rechazos(rechazos)
        escribir_resumen(total, len(validos), len(rechazos), por_categoria)
        verificar(total, len(validos), len(rechazos), por_categoria)
        registrar_ejecucion(total, len(validos), len(rechazos))
    except FileNotFoundError as error:
        print(f"No se encontró el archivo: {error.filename}")
        return
    except EncabezadoInvalido as error:
        print(error)
        return
    print("Total:", total, "| Válidos:", len(validos), "| Rechazados:", len(rechazos))
    print("Por categoría:", por_categoria)
    print("Verificación de salidas: OK")

if __name__ == "__main__":
    main()