# -*- coding: utf-8 -*-
"""proyecto

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AuF00cSdnsQTACnmfQ9aL6I_T2xa3pfU
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Leer el dataset desde un archivo CSV
df = pd.read_csv("Fuel.csv")
df.head(5)

# Verificar la estructura del DataFrame
df.head()
print(df.columns)

# Eliminar el espacio adicional en el nombre de la columna
df.rename(columns={'COEMISSIONS ': 'COEMISSIONS'}, inplace=True)

# Separar las características (X) y la etiqueta (y)
x = df[['COEMISSIONS', 'ENGINE SIZE', 'CYLINDERS']].values
y = df['FUEL CONSUMPTION'].values

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Generar el modelo y entrenarlo con el conjunto de entrenamiento
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Observar los parámetros hallados por el modelo
a0 = regressor.intercept_
a1 = regressor.coef_
print("Parámetros: interseccion = {}, pendiente = {}".format(a0, a1))

# Visualizar los datos de entrenamiento en 3D
fig_train = plt.figure()
ax_train = fig_train.add_subplot(111, projection='3d')

# Datos de entrenamiento
ax_train.scatter(X_train[:, 0], X_train[:, 1], y_train, color='green', label='Entrenamiento')

# Crear un meshgrid para el plano
x = np.linspace(df['COEMISSIONS'].min(), df['COEMISSIONS'].max(), num=10)
y = np.linspace(df['ENGINE SIZE'].min(), df['ENGINE SIZE'].max(), num=10)
x, y = np.meshgrid(x, y)

# Calcular los valores z (Fuel Consumption) del plano
z = regressor.intercept_ + regressor.coef_[0] * x + regressor.coef_[1] * y + regressor.coef_[2] * 4  # Asumir un valor promedio para CYLINDERS

# Graficar el plano
ax_train.plot_surface(x, y, z, alpha=0.5, color='gray')

ax_train.set_xlabel('COEMISSIONS')
ax_train.set_ylabel('ENGINE SIZE')
ax_train.set_zlabel('Fuel Consumption')
ax_train.set_title('Datos de Entrenamiento')
plt.legend()
plt.show()

# Visualizar los datos de prueba en 3D
fig_test = plt.figure()
ax_test = fig_test.add_subplot(111, projection='3d')

# Datos de prueba
ax_test.scatter(X_test[:, 0], X_test[:, 1], y_test, color='orange', label='Prueba')

# Crear un meshgrid para el plano
x = np.linspace(df['COEMISSIONS'].min(), df['COEMISSIONS'].max(), num=10)
y = np.linspace(df['ENGINE SIZE'].min(), df['ENGINE SIZE'].max(), num=10)
x, y = np.meshgrid(x, y)

# Calcular los valores z (Fuel Consumption) del plano
z = regressor.intercept_ + regressor.coef_[0] * x + regressor.coef_[1] * y + regressor.coef_[2] * 4  # Asumir un valor promedio para CYLINDERS

# Graficar el plano
ax_test.plot_surface(x, y, z, alpha=0.5, color='gray')

ax_test.set_xlabel('COEMISSIONS')
ax_test.set_ylabel('ENGINE SIZE')
ax_test.set_zlabel('Fuel Consumption')
ax_test.set_title('Datos de Prueba')
plt.legend()
plt.show()

# Calcular el desempeño del modelo
score = regressor.score(X_test, y_test)
print("Desempeño del modelo:", score)

# Prediciendo con una muestra nueva
new_sample = [[251, 1.8, 4]]
prediction = regressor.predict(new_sample)
print("Predicción para una nueva muestra:", prediction)