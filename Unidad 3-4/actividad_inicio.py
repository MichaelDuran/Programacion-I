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