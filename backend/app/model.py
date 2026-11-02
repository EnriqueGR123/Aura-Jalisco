# Importamos las herramientas que necesitamos
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

archivo = "datos_nasa.csv"


# Buscamos la fila donde empiezan los datos de verdad
with open(archivo, "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f):
        if linea.strip().startswith("YEAR,MO,DY"):
            fila_inicio = numero
            break


# Leemos el archivo desde la fila donde aparecen las columnas
datos = pd.read_csv(archivo, skiprows=fila_inicio)


# Eliminamos los registros que tienen -999, porque significa que no hay dato
datos = datos.replace(-999, np.nan)
datos = datos.dropna()


# Creamos una columna con la fecha completa
datos["fecha"] = pd.to_datetime(
    datos[["YEAR", "MO", "DY"]].rename(
        columns={"YEAR": "year", "MO": "month", "DY": "day"}
    )
)


# Obtenemos el número de día del año (del 1 al 365 o 366)
datos["dia_anio"] = datos["fecha"].dt.dayofyear


# Convertimos el día del año en dos valores para representar mejor las estaciones
# Esto ayuda a que diciembre y enero se consideren meses cercanos
datos["dia_sin"] = np.sin(2 * np.pi * datos["dia_anio"] / 365.25)
datos["dia_cos"] = np.cos(2 * np.pi * datos["dia_anio"] / 365.25)


# X contiene los datos que usará el modelo para aprender
X = datos[["dia_sin", "dia_cos"]]


# y contiene lo que queremos que el modelo prediga:
# la irradiación solar diaria
y = datos["ALLSKY_SFC_SW_DWN"]


# Separamos los datos por fecha:
# usamos el 80% más antiguo para entrenar y el 20% más reciente para probar
corte = int(len(datos) * 0.80)

X_entrenamiento = X.iloc[:corte]
X_prueba = X.iloc[corte:]

y_entrenamiento = y.iloc[:corte]
y_prueba = y.iloc[corte:]


# Creamos el árbol de decisión
modelo = DecisionTreeRegressor(
    max_depth=5,          # Limita el tamaño del árbol
    min_samples_leaf=20,  # Evita que aprenda de muy pocos registros
    random_state=42       # Permite repetir el mismo resultado
)


# Entrenamos el modelo con los datos históricos
modelo.fit(X_entrenamiento, y_entrenamiento)


# Le pedimos al modelo que haga predicciones con los datos de prueba
predicciones = modelo.predict(X_prueba)


# Calculamos qué tan bien funcionó el modelo
mae = mean_absolute_error(y_prueba, predicciones)
rmse = np.sqrt(mean_squared_error(y_prueba, predicciones))
r2 = r2_score(y_prueba, predicciones)

print("Resultados del modelo:")
print("Error MAE:", mae)
print("Error RMSE:", rmse)
print("R2:", r2)


# Guardamos el modelo entrenado para utilizarlo después desde FastAPI
joblib.dump(modelo, "modelo_solar.pkl")

print("Modelo guardado correctamente.")