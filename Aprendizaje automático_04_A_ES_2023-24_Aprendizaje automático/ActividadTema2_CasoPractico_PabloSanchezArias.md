```python
# Importar las bibliotecas necesarias
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Cargar el conjunto de datos Iris
iris_dataset = load_iris()

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

# Paso 1: Preparación de los datos
# En este paso, se cargan los datos del conjunto de datos Iris. Luego, se dividen los datos en conjuntos de entrenamiento
# y prueba utilizando la función train_test_split. Esto es esencial para evaluar el rendimiento del modelo en datos no vistos.

# Crear un modelo KNN (K-Nearest Neighbors)
knn = KNeighborsClassifier(n_neighbors=1)

# Paso 2: Selección del modelo
# Aquí se elige el modelo de clasificación KNN. En este caso, se configura el hiperparámetro n_neighbors en 1,
# lo que significa que se considera el vecino más cercano para realizar predicciones.

# Entrenar el modelo utilizando el conjunto de entrenamiento
knn.fit(X_train, y_train)

# Paso 3: Entrenamiento del modelo
# En este paso, el modelo KNN se entrena utilizando el conjunto de entrenamiento. El modelo aprenderá los patrones
# en los datos que le permitirán hacer predicciones precisas en datos nuevos.

# Evaluar el rendimiento del modelo en el conjunto de prueba
print("Score del test: {:.2f}".format(knn.score(X_test, y_test)))

# Paso 4: Evaluación del modelo
# Finalmente, se evalúa el rendimiento del modelo utilizando el conjunto de prueba. La función score() devuelve
# la precisión del modelo en los datos de prueba. Este valor es una métrica importante para medir el rendimiento
# y la capacidad de generalización del modelo.

# En resumen, este código ilustra los pasos fundamentales de un modelo de aprendizaje automático: Preparación de los datos,
# Selección del modelo, Entrenamiento del modelo y Evaluación del modelo.
```