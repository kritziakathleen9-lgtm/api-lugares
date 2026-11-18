# 🌍 Mi API de Lugares para Visitar

## 📌 Descripción

Este proyecto consiste en una API REST desarrollada con **Python y FastAPI** que permite gestionar un catálogo de lugares que me gustaría visitar alrededor del mundo.

La API permite consultar, agregar, editar y eliminar destinos turísticos. También incluye funcionalidades adicionales como filtrar lugares por país, validar presupuestos y evitar destinos duplicados.

Los datos se almacenan en un archivo JSON, por lo que los cambios se mantienen guardados incluso después de reiniciar el servidor.

## 🛠️ Tecnologías utilizadas

- **Python 3.14**
- **FastAPI:** creación de la API REST.
- **Pydantic:** validación de datos.
- **JSON:** almacenamiento de los destinos.
- **Uvicorn:** servidor de desarrollo.
- **Swagger UI:** documentación y pruebas de las rutas.
- **Git y GitHub:** control de versiones.

## 📁 Estructura del proyecto

```text
api-lugares/
├── main.py
├── lugares.json
├── requirements.txt
├── README.md
└── .gitignore
```

- `main.py`: contiene la lógica de la API y sus rutas.
- `lugares.json`: almacena los destinos turísticos.
- `requirements.txt`: contiene las dependencias del proyecto.
- `README.md`: documentación del proyecto.
- `.gitignore`: evita subir archivos innecesarios, como el entorno virtual.

## 🚀 Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone https://github.com/kritziakathleen9-lgtm/api-lugares.git
cd api-lugares
```

**2. Crear un entorno virtual con Python 3.14**

```bash
py -3.14 -m venv .venv
```

**3. Activar el entorno virtual**

En Git Bash (Windows):

```bash
source .venv/Scripts/activate
```

**4. Instalar las dependencias**

```bash
python -m pip install -r requirements.txt
```

**5. Iniciar el servidor**

```bash
fastapi dev main.py
```

**6. Abrir la documentación interactiva**

Una vez iniciado el servidor, acceder a:

http://127.0.0.1:8000/docs

Desde Swagger UI se pueden probar todas las rutas de la API.

## 📍 Rutas de la API

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/lugares` | Listar todos los destinos |
| GET | `/lugares/{id}` | Buscar un destino por ID |
| POST | `/lugares` | Agregar un nuevo destino |
| PUT | `/lugares/{id}` | Editar un destino existente |
| DELETE | `/lugares/{id}` | Eliminar un destino |

### Ejemplo de un destino

```json
{
  "id": 1,
  "ciudad": "Edimburgo",
  "pais": "Reino Unido",
  "presupuesto": 1000,
  "descripcion": "Visitar el Castillo de Edimburgo, recorrer la Royal Mile y conocer Arthur's Seat"
}
```

Cada destino contiene:

- `id`: identificador único generado
