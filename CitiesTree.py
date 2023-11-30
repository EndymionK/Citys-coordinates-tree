import matplotlib.pyplot as plt
import math
import time
import random
from tqdm import tqdm

class Node:
    def __init__(self, city, coordinates, distance=0):
        self.city = city
        self.latitude, self.longitude = coordinates
        self.distance = distance
        self.left = None
        self.right = None

def read_csv(file_path, encoding='utf-8'):
    data = []
    with open(file_path, 'r', encoding=encoding) as file:
        next(file)  # Skip header
        for line in file:
            city, latitude, longitude = line.strip().split(',')
            coordinates = (float(latitude), float(longitude))
            node = Node(city, coordinates)
            data.append(node)
    return data

def build_kdb_tree_with_limit(data, depth=0, parent=None, limit=None):
    if not data or (limit is not None and len(data) > limit):
        return None

    axis = depth % 2
    data.sort(key=lambda x: getattr(x, 'latitude' if axis == 0 else 'longitude'))

    median = len(data) // 2
    node = Node(data[median].city, (data[median].latitude, data[median].longitude), distance=0)

    if parent is not None:
        node.distance = haversine(node.latitude, node.longitude, parent.latitude, parent.longitude)

    node.left = build_kdb_tree_with_limit(data[:median], depth + 1, parent=node, limit=limit)
    node.right = build_kdb_tree_with_limit(data[median + 1:], depth + 1, parent=node, limit=limit)

    return node

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def adjust_longitude_distance(latitude):
    equator_circumference = 40075.0
    return equator_circumference * math.cos(math.radians(latitude)) / 360.0

def find_nearest_cities(node, target, num_cities=5, depth=0, best_cities=None):
    if best_cities is None:
        best_cities = [{'city': None, 'coordinates': None, 'distance': float('inf')} for _ in range(num_cities)]

    if node is not None:
        axis = depth % 2
        if axis == 0:
            next_branch = node.left if target[axis] < node.latitude else node.right
        else:
            next_branch = node.left if target[axis] < node.longitude else node.right

        opposite_branch = node.right if next_branch is node.left else node.left

        find_nearest_cities(next_branch, target, num_cities, depth + 1, best_cities)

        distance_to_target = haversine(node.latitude, node.longitude, target[0], target[1])
        adjusted_longitude_distance = adjust_longitude_distance(node.latitude)

        for i, city_info in enumerate(best_cities):
            if distance_to_target < city_info['distance']:
                best_cities.insert(i, {'city': node.city, 'coordinates': (node.latitude, node.longitude), 'distance': distance_to_target})
                best_cities.pop()
                break

        if len(best_cities) < num_cities or opposite_branch is not None:
            find_nearest_cities(opposite_branch, target, num_cities, depth + 1, best_cities)

    return best_cities

def clean_city_name(city_name):
    return ''.join(c if c.isalnum() else '_' for c in city_name).lower()

def plot_kdb_tree_dynamic(node, axis, parent_rect, depth=0):
    if node is not None:
        if axis == 0:
            rect = [parent_rect[0], parent_rect[1], node.longitude, parent_rect[3]]
            plt.plot([node.longitude, node.longitude], [parent_rect[1], parent_rect[3]], color='black')
        else:
            rect = [parent_rect[0], parent_rect[1], parent_rect[2], node.latitude]
            plt.plot([parent_rect[0], parent_rect[2]], [node.latitude, node.latitude], color='black')

        plt.pause(1)
        plt.draw()

        plot_kdb_tree_dynamic(node.left, 1 - axis, rect, depth + 1)
        plot_kdb_tree_dynamic(node.right, 1 - axis, rect, depth + 1)

# Obtener coordenadas al azar limitando a 1,000 registros
random.seed(42)
file_path = r'D:\Proyectos programación\Citys-coordinates-tree\Databases\cleardata.csv'
city_data = read_csv(file_path)
coordinates_data = [Node(city=node.city, coordinates=(node.latitude, node.longitude)) for node in city_data]

user_cantidad = int(input("Ingrese la cantidad de ciudades para construir el arbol (No debe ser superior a 2.2M): "))
random_coordinates = random.sample(coordinates_data, user_cantidad)

# Construir el árbol KDB con límite y mostrar la barra de progreso

for _ in tqdm(range(10000), desc="Building KDB Tree"):
    time.sleep(0.0001)
kdb_tree = build_kdb_tree_with_limit(random_coordinates)
print("Árbol KDB construido con éxito")

# Obtener coordenadas del usuario por consola
user_latitude = float(input("Ingrese la latitud (-90 a 90): "))
user_longitude = float(input("Ingrese la longitud (-180 a 180): "))
user_target_coordinates = (user_latitude, user_longitude)

# Encontrar las ciudades más cercanas
nearest_cities = find_nearest_cities(kdb_tree, user_target_coordinates)

# Mostrar las 5 ciudades más cercanas
print("\nLas 5 ciudades más cercanas son:")
for city_info in nearest_cities:
    print(f"Nombre: {city_info['city']}, Coordenadas: {city_info['coordinates']}, Distancia: {city_info['distance']} km")

def count_levels(node, depth=0):
    if node is None:
        return depth
    left_levels = count_levels(node.left, depth + 1)
    right_levels = count_levels(node.right, depth + 1)
    return max(left_levels, right_levels)


kdb_tree = build_kdb_tree_with_limit(random_coordinates)

# Imprime la cantidad de niveles
num_levels = count_levels(kdb_tree)
print(f"La cantidad de niveles del árbol KDB es: {num_levels}")

# Configurar el gráfico
plt.ion()
plt.figure(figsize=(10, 6))
plt.scatter([node.longitude for node in random_coordinates], [node.latitude for node in random_coordinates], color='blue', label='Ciudades', s=10)
plt.scatter(user_longitude, user_latitude, color='red', marker='x', label='Usuario')

# Plotear las divisiones del árbol KDB dinámicamente
plot_kdb_tree_dynamic(kdb_tree, 0, [-180, -90, 180, 90])

plt.title('Árbol KDB y Divisiones del Espacio')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.legend()

# Desactivar el modo interactivo al final
plt.ioff()
plt.show()
