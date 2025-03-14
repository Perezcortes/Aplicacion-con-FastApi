# Importar FastAPI y HTMLResponse para crear la aplicación y manejar respuestas HTML
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

# Crear una instancia de la aplicación
app = FastAPI()

# Lista de películas (datos de ejemplo)
movies = [
  {
    "id": 1,
    "title": "Avatar",
    "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
    "year": "2009",
    "rating": 7.8,
    "category": "Acción"
  },
  {
    "id": 2,
    "title": "Son como niños",
    "overview": "Adultos que actuan como niños y hacen desastres ...",
    "year": "2009",
    "rating": 7.8,
    "category": "Comedia"
  }
]

# Configurar el título y la versión de la aplicación
app.title = "Aplicacion con FastApi"
app.version = "2.0.0"

# Definir una ruta GET en la raíz (/)
@app.get('/', tags=['Home'])
def home():
    # Devolver un mensaje simple como respuesta
    return "Hola FastApi!"

# Ruta GET en /home
@app.get('/home', tags=['Home']) #Nuevo endpoint
def home():
    # Devolver un mensaje simple como respuesta
    return "Hola FastApi!"
""""
@app.get('/movies', tags=['Movies'])
def home():
    return {"Hello": "FastApi"}"
"""
""""
@app.get('/movies', tags=['Movies'])
def home():
    return HTMLResponse('<h1>¡Hola FastAPI!</h1>')
"""
"""
# Ruta GET en /movies para obtener todas las películas
@app.get('/movies', tags=['Movies'])
def home():
    # Devuelve la lista completa de películas
    return movies
"""
"""
#parametros de ruta
@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    return id
"""

@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies
# Ruta GET en /movies/{id} para obtener una película por su ID
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    # Busca la película por ID y la devuelve
    for movie in movies:
        if movie['id'] == id:
            return movie
    # Si no encuentra la película, devuelve una lista vacía
    return []

#Parametros Query
"""
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str):
    return category
"""
"""
#Mas de un parametros Query
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int):
    return year"
"""

@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie['category'] == category:
            return movie
    # Si no encuentra la película, devuelve una lista vacía
    return []

#Metodo POST en FastApi
@app.post('/movies', tags=['Movies'])
def create_movie(
    id: int = Body(), 
    title: str = Body(), 
    overview: str = Body(), 
    year: int = Body(), 
    rating: float = Body(), 
    category: str = Body()
    ):
    movies.append({
        'id': id,
        'title': title,
        overview: overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(
    id: int,
    title: str = Body(), 
    overview: str = Body(), 
    year: int = Body(), 
    rating: float = Body(), 
    category: str = Body()
):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
    return movies


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies