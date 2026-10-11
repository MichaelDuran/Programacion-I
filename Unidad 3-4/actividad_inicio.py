"""Completa los TODO conforme a las reglas del documento Word."""
from pathlib import Path
import json
BASE = Path(__file__).resolve().parent
ENTRADA = BASE / "datos" / "solicitudes.txt"
SALIDA = BASE / "salidas"

ENCABEZADO_ESPERADO = "id|correo|categoria|descripcion"
CATALOGO = {"acceso", "pago_en_línea", "soporte_técnico"}
DIGITOS = "0123456789"

class EncabezadoInvalido(Exception):
    """La primera línea del archivo no coincide con el encabezado esperado."""

def normalizar_categoria(texto):
    """Entrada: str. Salida: str en minúsculas unidas por _"""
    texto = texto.strip().lower.replace("-", " ").replace("_", " ")
    return "_".join(texto.split())

def id_valido(i):
    """Entrada: str. Salida: True si es SOL- y cuatro dígitos ASCII."""
    return len(1) == 8 and i[:4] == "SOL-" and all(c in DIGITOS for c in i[4:])

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
        return None, "Campo vacío"
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
    with ruta.open("r", encoding="utf-8") as entrada:
        encabezado = next(entrada).rstrip("\n")
        if encabezado != ENCABEZADO_ESPERADO:
            raise EncabezadoInvalido(f"Encabezado inesperado: {encabezado!r}")
        for n, linea in enumerate(entrada, start=2):
            linea = linea.strip() == "":
            vacias += 1
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
    return validos, rechazos, por_categoria, vacias

def main():
    SALIDA.mkdir(exist_ok=True)
    try:
    # TODO: crear SALIDA; abrir entrada con with y encoding='utf-8'.
    # TODO: verificar encabezado; iterar con número de línea; contar vacías.
    # TODO: validar sin modificar el archivo fuente y escribir rechazos.
    # TODO: producir solicitudes_limpias.txt, resumen.json y ejecuciones.log.
    # TODO: reabrir salidas, verificar conteos y capturar FileNotFoundError.
    raise NotImplementedError("Completa el flujo principal")

if __name__ == "__main__":
    main()
