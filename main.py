
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI(title="Mi API de Lugares para Visitar")

ARCHIVO = Path(__file__).with_name("lugares.json")


class Lugar(BaseModel):
    ciudad: str
    pais: str
    presupuesto: int
    descripcion: str


def leer_lugares():
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


@app.get("/lugares")
def listar_lugares():
    return leer_lugares()


@app.get("/lugares/{id}")
def buscar_lugar(id: int):
    lugares = leer_lugares()

    for lugar in lugares:
        if lugar["id"] == id:
            return lugar

    raise HTTPException(
        status_code=404,
        detail="Lugar no encontrado"
    )


@app.post("/lugares", status_code=201)
def agregar_lugar(lugar: Lugar):
    lugares = leer_lugares()

    nuevo_id = max(
        (destino["id"] for destino in lugares),
        default=0
    ) + 1

    nuevo_lugar = {
        "id": nuevo_id,
        **lugar.model_dump()
    }

    lugares.append(nuevo_lugar)

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(lugares, archivo, ensure_ascii=False, indent=4)

    return nuevo_lugar


@app.put("/lugares/{id}")
def editar_lugar(id: int, lugar: Lugar):
    lugares = leer_lugares()

    for indice, destino in enumerate(lugares):
        if destino["id"] == id:
            lugar_actualizado = {
                "id": id,
                **lugar.model_dump()
            }

            lugares[indice] = lugar_actualizado

            with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(lugares, archivo, ensure_ascii=False, indent=4)

            return lugar_actualizado

    raise HTTPException(
        status_code=404,
        detail="Lugar no encontrado"
    )


@app.delete("/lugares/{id}")
def eliminar_lugar(id: int):
    lugares = leer_lugares()

    for lugar in lugares:
        if lugar["id"] == id:
            lugares.remove(lugar)

            with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(lugares, archivo, ensure_ascii=False, indent=4)

            return {"mensaje": "Lugar eliminado correctamente"}

    raise HTTPException(
        status_code=404,
        detail="Lugar no encontrado"
    )
