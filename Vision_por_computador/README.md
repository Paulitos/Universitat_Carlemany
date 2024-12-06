Docente: Guilem Cobos Zara

Grades:  
Quiz 1 -> 8  

Durante este quiz de visión por computadora, aprendí a trabajar con imágenes utilizando Python y OpenCV, incluyendo conceptos fundamentales como el sistema de coordenadas de las imágenes, donde `(0,0)` se encuentra en la esquina superior izquierda y se avanza en el eje `x` hacia la derecha y en el eje `y` hacia abajo. Comprendí cómo obtener las dimensiones de las imágenes mediante `img.shape`, que retorna altura, ancho y canales, y que OpenCV carga imágenes por defecto en el espacio de color BGR, con posibilidad de convertirlas a escala de grises o RGB usando `cv2.cvtColor`. Aprendí a redimensionar imágenes con `cv2.resize`, tanto ajustando proporcionalmente como especificando dimensiones concretas, y a realizar recortes con índices NumPy `[inicio_y:fin_y, inicio_x:fin_x]` para extraer regiones específicas. Profundicé en la detección de contornos con `cv2.findContours`, especialmente con `cv2.RETR_EXTERNAL` para contornos externos y `cv2.CHAIN_APPROX_SIMPLE` para optimización, apoyándome en pasos previos como la conversión a escala de grises y la umbralización (`cv2.threshold`) para mejorar la detección. Además, practiqué la visualización de imágenes procesadas y resultados usando bibliotecas como Matplotlib, permitiendo analizar y presentar los efectos de las operaciones realizadas. En resumen, consolidé habilidades clave para manipular imágenes, procesarlas y detectar características importantes, como contornos, en el contexto de visión por computadora.

Quiz 2 -> 5  

Durante este quiz de visión por computadora, aprendí a utilizar redes neuronales multicapa para tareas de clasificación de imágenes, específicamente con el conjunto de datos MNIST. Comprendí cómo configurar un `MLPClassifier` de Scikit-learn, ajustando parámetros como el número de capas ocultas, la función de activación y los optimizadores (`adam` y `sgd`). Exploré cómo el tamaño de las capas y el tipo de optimizador afectan la precisión y el rendimiento del modelo. También profundicé en el preprocesamiento de imágenes externas, asegurando el formato adecuado (escala de grises, normalización y redimensionamiento a \(28 \times 28\)) para que puedan ser clasificadas correctamente. En resumen, aprendí a entrenar y evaluar redes neuronales simples y a integrarlas con imágenes personalizadas en el flujo de trabajo de visión por computadora.

Quiz 3 -> 8  

En este quiz se evaluaron modelos YOLOv8 en imágenes usando formatos **BGR** y **RGB**, analizando diferencias en predicciones, niveles de confianza y detección de clases como personas y objetos. Se observó que **BGR** suele tener mayores niveles de confianza, pero el número de detecciones es igual en ambos formatos.

