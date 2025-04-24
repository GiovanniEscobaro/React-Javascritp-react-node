# Importamos librerías
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Datos: Tamaño (m²) y Precio (USD)
X = [[50], [60], [70], [80], [90], [100], [110]]
y = [100000, 120000, 140000, 160000, 180000, 200000, 220000]

# Dividimos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el modelo
modelo = LinearRegression()

# Entrenamos el modelo
modelo.fit(X_train, y_train)

# Hacemos predicciones con los datos de prueba
y_pred = modelo.predict(X_test)

# Mostramos resultados
print("Predicciones:", y_pred)
print("Valores reales:", y_test)
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))

# Predecimos el precio de una casa de 95 m²
precio_95 = modelo.predict([[95]])
print("Precio estimado para 95 m²:", precio_95[0])