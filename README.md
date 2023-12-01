
Análisis y Solución del Problema de Rutas y Navegación GPS con Árboles
Definición del Problema:
El problema plantea la necesidad de encontrar la ruta más corta entre dos puntos en un conjunto de ciudades utilizando árboles. Aunque la estructura jerárquica elegida es un Árbol de Búsqueda K-Dimensional (KDB), surge la necesidad de considerar nodos dirigidos para tener en cuenta las vías y carreteras en la planificación de rutas.

Elección de la Estructura Jerárquica:
Optamos por un Árbol de Búsqueda K-Dimensional (KDB), un tipo de árbol binario optimizado para búsqueda espacial en dimensiones múltiples. Sin embargo, es crucial tener en cuenta que este enfoque se centra en la eficiencia en búsquedas espaciales, pero no considera la dirección de las vías.

Justificación de la Elección del Árbol Binario:
Eficiencia en Búsquedas Espaciales: El árbol binario permite dividir eficientemente el espacio, facilitando la búsqueda de ciudades cercanas según sus coordenadas.

División por Coordenadas: Al alternar entre coordenadas de latitud y longitud en cada nivel, el KDB mejora la eficiencia en conjuntos de datos geoespaciales.

Nota sobre Nodos Dirigidos:
Para abordar completamente la planificación de rutas y navegación GPS, se requeriría la inclusión de nodos dirigidos que representen las vías y carreteras entre las ciudades. Este enfoque permitiría considerar las direcciones y restricciones de las vías al determinar la ruta más corta.

Implementación del Árbol KDB:
La implementación utiliza la clase Node para representar ciudades con coordenadas. La función build_kdb_tree_with_limit construye el árbol de manera recursiva, dividiendo el espacio según las coordenadas y eligiendo la mediana para una división equitativa.

Búsqueda de Ciudades Cercanas:
La función find_nearest_cities aprovecha la estructura del árbol para reducir el espacio de búsqueda y encontrar ciudades cercanas al punto proporcionado.

Visualización del Árbol KDB:
Matplotlib se emplea para visualizar dinámicamente la estructura del árbol KDB, mostrando cómo se divide el espacio en cada nivel.

Entrada del Usuario y Evaluación:
Se solicita al usuario ingresar la cantidad de ciudades y sus coordenadas para construir el árbol. La progresión del proceso de construcción se muestra. Posteriormente, se pide al usuario ingresar sus propias coordenadas para encontrar las ciudades más cercanas.

Resultados y Conclusión:
Se presentan las 5 ciudades más cercanas al usuario, con coordenadas y distancias. Además, se imprime la cantidad de niveles del árbol KDB para evaluar su complejidad.

Visualización Gráfica:
Se genera un gráfico con ciudades, la ubicación del usuario y las divisiones dinámicas del árbol KDB.
