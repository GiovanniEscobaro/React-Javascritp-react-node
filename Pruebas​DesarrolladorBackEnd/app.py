# Importamos Flask para crear la API y pandas para manejar el archivo CSV
from flask import Flask, request, jsonify
import pandas as pd

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Leemos el archivo CSV de películas al iniciar la aplicación
# Se asume que el archivo 'movies.csv' está en el mismo directorio
df = pd.read_csv('movies.csv')

# Definimos la ruta '/movie' que acepta el método GET para buscarla.
@app.route('/movie', methods=['GET'])
def get_movie_by_id():
    """
    Servicio REST para obtener los datos de una película por su ID.
    Recibe el parámetro 'id' por la URL y retorna los datos en formato JSON.
    Ejemplo de solicitud: GET /movie?id=7
    """
    try:
        # Se intenta obtener el parámetro 'id' de la URL y convertirlo a entero
        movie_id = int(request.args.get('id'))
    except (ValueError, TypeError):
        # Si el ID no es válido o no se proporciona, retorna un error 400
        return jsonify({'error': 'ID inválido'}), 400

    # Filtramos el DataFrame para encontrar la película con el ID dado
    movie = df[df['ID'] == movie_id]

    # Si no se encuentra ninguna película con ese ID, retorna error 404
    if movie.empty:
        return jsonify({'error': 'Película no encontrada'}), 404

    # Extraemos los datos de la película como un diccionario
    row = movie.iloc[0]
    return jsonify({
        'id': int(row['ID']),
        'film': row['Film'],
        'genre': row['Genre'],
        'studio': row['Studio'],
        'score': int(row['Score']),
        'year': int(row['Year'])
    })

# Definimos la ruta '/movie' que acepta el método GET para ordenala.

@app.route('/movies', methods=['GET'])
def list_movies_ordered():
    """
    Servicio REST que retorna una lista de películas ordenadas alfabéticamente por el nombre del film.
    Parámetros por URL:
    - total: cantidad máxima de resultados a retornar.
    - order: 'asc' para orden ascendente, 'desc' para descendente.
    
    Ejemplo de solicitud:
    GET /movies?total=3&order=asc
    """
    total = request.args.get('total')
    order = request.args.get('order', 'asc')

    # Validación de parámetro 'total'
    try:
        total = int(total)
        if total <= 0:
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetro "total" inválido'}), 400

    # Validación de parámetro 'order'
    if order not in ['asc', 'desc']:
        return jsonify({'error': 'Parámetro "order" debe ser "asc" o "desc"'}), 400

    # Ordenar el DataFrame por la columna 'Film'
    sorted_df = df.sort_values(by='Film', ascending=(order == 'asc'))

    # Seleccionar los primeros 'total' elementos
    movies = sorted_df.head(total)

    # Convertir los resultados a una lista de diccionarios
    result = [
        {
            'id': int(row['ID']),
            'film': row['Film'],
            'genre': row['Genre'],
            'studio': row['Studio'],
            'score': int(row['Score']),
            'year': int(row['Year'])
        }
        for _, row in movies.iterrows()
    ]

    return jsonify(result)


#Definimos la ruta '/movie' que acepta el método POST para adicionar nueva pelicula.

@app.route('/movie', methods=['POST'])
def add_movie():
    """
    Servicio REST que permite agregar una nueva película al dataset.
    Método: POST
    Cuerpo JSON esperado:
    {
        "id": 78,
        "film": "Parasite",
        "genre": "Drama",
        "studio": "Barunson E&A",
        "score": 97,
        "year": 2019
    }
    """
    global df
    new_movie = request.get_json()

    # Validar que todos los campos requeridos estén presentes
    required_fields = {'id', 'film', 'genre', 'studio', 'score', 'year'}
    if not all(field in new_movie for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    # Verificar si ya existe una película con ese ID
    if int(new_movie['id']) in df['ID'].values:
        return jsonify({'error': 'El ID ya existe'}), 400

    # Agregar la película al DataFrame global
    
    df = pd.concat([df, pd.DataFrame([{
        'ID': int(new_movie['id']),
        'Film': new_movie['film'],
        'Genre': new_movie['genre'],
        'Studio': new_movie['studio'],
        'Score': int(new_movie['score']),
        'Year': int(new_movie['year'])
    }])], ignore_index=True)

    return jsonify({'message': 'La película fue creada con éxito'}), 201


# Punto de entrada de la aplicación
# Se ejecuta el servidor Flask en el puerto 8080 con modo debug activado
if __name__ == '__main__':
    app.run(debug=True, port=8080)