# 🌍 Mi API de Lugares para Visitar

## Descripción

Este proyecto es una API REST desarrollada con Python y FastAPI que permite gestionar un catálogo de lugares que me gustaría visitar.

La API permite consultar, agregar, editar y eliminar destinos turísticos. La información se almacena en un archivo JSON para conservar los cambios incluso después de reiniciar el servidor.

## Tecnologías utilizadas

- Python 3.14
- FastAPI
- Pydantic
- JSON
- Uvicorn

## Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone URL_DEL_REPOSITORIO
cd api-lugares
```

**2. Crear el entorno virtual**

```bash
py -3.14 -m venv .venv
```

**3. Activar el entorno virtual en Git Bash (Windows)**

```bash
source .venv/Scripts/activate
```

**4. Instalar las dependencias**

```bash
python -m pip install -r requirements.txt
```

**5. Iniciar el servidor**

```bash
python -m uvicorn main:app --reload
```

**6. Abrir la documentación**

http://127.0.0.1:8000/docs

## Rutas de la API

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/lugares` | Listar todos los lugares |
| GET | `/lugares/{id}` | Buscar un lugar por ID |
| POST | `/lugares` | Agregar un nuevo lugar |
| PUT | `/lugares/{id}` | Editar un lugar existente |
| DELETE | `/lugares/{id}` | Eliminar un lugar |

## Ejemplo de un destino

```json
{
  "id": 1,
  "ciudad": "Edimburgo",
  "pais": "Reino Unido",
  "presupuesto": 800,
  "descripcion": "Visitar el Castillo de Edimburgo y recorrer la Royal Mile"
}
```

## Funcionalidades

- Catálogo inicial de cinco destinos turísticos.
- Validación de datos mediante Pydantic.
- Generación automática de ID al agregar un lugar.
- Respuestas 404 cuando un destino no existe.
- Almacenamiento persistente en `lugares.json`.
- Documentación interactiva con Swagger UI.

## Autoría

Proyecto individual desarrollado como práctica de FastAPI.
