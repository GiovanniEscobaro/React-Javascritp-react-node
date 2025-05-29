import pytest
from app import app, df  # Importa la app y el dataframe original
import json
##--Estructura del archivo de pruebas test_app.py--
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

##--Pruebas para /movie?id=ID (GET una película por ID)--
def test_get_movie_by_id_success(client):
    """
    Prueba que el endpoint /movie devuelve correctamente una película existente por su ID.
    """
    response = client.get('/movie?id=1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert 'film' in data

def test_get_movie_by_id_not_found(client):
    """
    Prueba que se devuelva un error 404 si la película no existe.
    """
    response = client.get('/movie?id=999999')
    assert response.status_code == 404
    assert 'error' in response.get_json()

def test_get_movie_by_id_invalid(client):
    """
    Prueba que se devuelva un error 400 si el ID no es válido.
    """
    response = client.get('/movie?id=abc')
    assert response.status_code == 400

##--Pruebas para /movies?total=N&order=asc|desc (listar películas)--
def test_list_movies_ordered_asc(client):
    """
    Prueba que las películas se devuelven en orden ascendente por título.
    """
    response = client.get('/movies?total=2&order=asc')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['film'] <= data[1]['film']

def test_list_movies_ordered_desc(client):
    """
    Prueba que las películas se devuelven en orden descendente por título.
    """
    response = client.get('/movies?total=2&order=desc')
    assert response.status_code == 200
    data = response.get_json()
    assert data[0]['film'] >= data[1]['film']

def test_list_movies_invalid_total(client):
    """
    Prueba que se devuelva error si 'total' no es un número válido.
    """
    response = client.get('/movies?total=abc&order=asc')
    assert response.status_code == 400

def test_list_movies_invalid_order(client):
    """
    Prueba que se devuelva error si el parámetro 'order' no es válido.
    """
    response = client.get('/movies?total=2&order=random')
    assert response.status_code == 400


##--Pruebas para POST /movie (agregar película)--

def test_add_movie_success(client):
    """
    Prueba que una película se puede agregar correctamente con POST.
    """
    new_movie = {
        "id": 12345,
        "film": "Unit Test Movie",
        "genre": "Test",
        "studio": "Test Studio",
        "score": 95,
        "year": 2024
    }
    response = client.post('/movie', json=new_movie)
    assert response.status_code == 201
    assert response.get_json()['message'] == 'La película fue creada con éxito'

    # Verificar que se puede consultar por ID luego
    get_response = client.get(f"/movie?id={new_movie['id']}")
    assert get_response.status_code == 200
    data = get_response.get_json()
    assert data['film'] == new_movie['film']

def test_add_movie_missing_fields(client):
    """
    Prueba que falten campos requeridos al hacer POST devuelve error 400.
    """
    response = client.post('/movie', json={"id": 8888, "film": "Incomplete"})
    assert response.status_code == 400

def test_add_movie_duplicate_id(client):
    """
    Prueba que no se permite agregar una película con un ID ya existente.
    """
    # Usa un ID que ya exista en el CSV, como 1
    movie = {
        "id": 1,
        "film": "Duplicado",
        "genre": "Drama",
        "studio": "Studio",
        "score": 50,
        "year": 2020
    }
    response = client.post('/movie', json=movie)
    assert response.status_code == 400
    assert 'ID ya existe' in response.get_json()['error']
