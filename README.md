Definición del Problema:

El problema aborda la planificación de rutas y navegación GPS para encontrar la ruta más corta entre dos puntos en un conjunto de datos de ciudades.
Elección de la Estructura Jerárquica:

Se optó por una estructura de árbol para organizar las ciudades y encontrar eficientemente la ruta más corta entre dos puntos.
Justificación de la Elección del Árbol Binario:

En este código, se implementa un Árbol de Búsqueda K-Dimensional (KDB), que es un tipo de árbol binario optimizado para búsqueda espacial en dimensiones múltiples. La elección de un árbol binario se debe a:
Eficiencia en Búsquedas Espaciales: Un árbol binario permite dividir el espacio de manera eficiente, facilitando la búsqueda de ciudades cercanas en función de coordenadas.
División por Coordenadas: El árbol se divide alternando entre coordenadas de latitud y longitud en cada nivel, mejorando la eficiencia de búsqueda en conjuntos de datos geoespaciales.
Implementación del Árbol KDB:

Se utiliza la clase Node para representar cada ciudad con sus coordenadas.
La función build_kdb_tree_with_limit construye el árbol KDB de manera recursiva, dividiendo el espacio según las coordenadas.
La elección de la mediana en cada nivel facilita la división equitativa del espacio.
Búsqueda de Ciudades Cercanas:

La función find_nearest_cities busca las ciudades más cercanas al punto proporcionado, utilizando la estructura del árbol para reducir el espacio de búsqueda.
Visualización del Árbol KDB:

Se emplea la biblioteca Matplotlib para visualizar dinámicamente la estructura del árbol KDB, mostrando cómo se divide el espacio en cada nivel.
Entrada del Usuario y Evaluación:

Se solicita al usuario ingresar la cantidad de ciudades para construir el árbol y sus coordenadas.
Se muestra la progresión del proceso de construcción del árbol.
Se pide al usuario ingresar sus propias coordenadas para encontrar las ciudades más cercanas.
Resultados y Conclusión:

Se presentan las 5 ciudades más cercanas al usuario, junto con sus coordenadas y distancias.
Se imprime la cantidad de niveles del árbol KDB para evaluar su complejidad.
Visualización Gráfica:

Se genera un gráfico con las ciudades, la ubicación del usuario y las divisiones dinámicas del árbol KDB.
Desactivación del Modo Interactivo:

Al finalizar, se desactiva el modo interactivo de Matplotlib.
