import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Cargar los datos
df = pd.read_csv("F:\SoftwareEstudio\Entrevistas\sales_data_python.csv", parse_dates=["Date"])

# Exploración inicial
print(df.info())
print(df.describe())
print(df.head())
print(df.isnull().sum())

# Extraer componentes de la fecha
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["WeekOfYear"] = df["Date"].dt.isocalendar().week.astype(int)

# Variable de ingresos
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

# Codificamos Store y Category para que el modelo pueda utilizarlas.
le_store = LabelEncoder()
le_category = LabelEncoder()

df["Store_encoded"] = le_store.fit_transform(df["Store"])
df["Category_encoded"] = le_category.fit_transform(df["Category"])


# Ordenar por fecha
df = df.sort_values("Date")

# Entrenamos con datos antes de una fecha (por ejemplo, último mes reservado para test)
split_date = "2024-12-01"
train = df[df["Date"] < split_date]
test = df[df["Date"] >= split_date]

# Selección de variables
features = ["Store_encoded", "Category_encoded", "Month", "Day", "DayOfWeek", "WeekOfYear", "Unit_Price"]
target = "Units_Sold"

X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]

#Usamos un modelo robusto como Random Forest Regressor.
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print(df["Date"].min(), df["Date"].max())
# Predicción
y_pred = model.predict(X_test)

# Evaluación
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse:.2f}")