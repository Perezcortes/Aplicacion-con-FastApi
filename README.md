
# 🚀 Aplicación con FastAPI - Gestión de Películas

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="300">
</p>


## Características

- **Framework**: **FastAPI** para crear una API RESTful.
- **Operaciones CRUD**:
  - `GET /movies`: Obtener todas las películas.
  - `GET /movies/{id}`: Obtener una película por ID.
  - `POST /movies`: Crear una nueva película.
  - `PUT /movies/{id}`: Actualizar la información de una película existente.
  - `DELETE /movies/{id}`: Eliminar una película por ID.
- **Documentación automática con Swagger**: FastAPI proporciona documentación automática e interactiva de la API utilizando **Swagger UI**. Accede a la documentación en [http://localhost:8000/docs](http://localhost:8000/docs).
- **Validación automática**: La aplicación valida los datos de entrada mediante el uso de modelos de Pydantic integrados en FastAPI.
- **Manejo de errores**: Errores y excepciones son manejados por middlewares personalizados.

## Requisitos

- **Python 3.7+**
- **FastAPI**
- **Uvicorn** (para correr el servidor)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/Perezcortes/Aplicacion-con-FastApi.git
    cd perezcortes-aplicacion-con-fastapi
    ```

2. Crea un entorno virtual y activa el entorno:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En sistemas Unix
    venv\Scripts\activate     # En Windows
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para iniciar el servidor de desarrollo, usa el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto ejecutará la aplicación en [http://localhost:8000](http://localhost:8000).

## Uso de la API

### Rutas disponibles:

- **`GET /movies`**: Obtiene todas las películas en la base de datos.
- **`GET /movies/{id}`**: Obtiene una película por ID.
- **`POST /movies`**: Crea una nueva película. Debes enviar los siguientes datos en el cuerpo de la solicitud:
    - `id`: (int)
    - `title`: (str)
    - `overview`: (str)
    - `year`: (int)
    - `rating`: (float)
    - `category`: (str)
- **`PUT /movies/{id}`**: Actualiza los detalles de una película por ID.
- **`DELETE /movies/{id}`**: Elimina una película por ID.

### Documentación Automática

FastAPI genera automáticamente documentación de la API que puedes visualizar de forma interactiva:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Contribuciones

Si deseas contribuir al proyecto, por favor abre un **pull request**. Asegúrate de seguir las mejores prácticas de desarrollo y agregar pruebas para nuevas funcionalidades.

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

**Desarrollado por:** Perezcortes  
**Correo:** [9531447499a@gmail.com](mailto:9531447499a@gmail.com)
