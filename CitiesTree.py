import math

class Node:
    def __init__(self, city, latitude, longitude, distance=0):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.left = None
        self.right = None

def read_csv(file_path, encoding='utf-8'):
    data = []
    with open(file_path, 'r', encoding=encoding) as file:
        next(file)  # Skip header
        for line in file:
            city, latitude, longitude = line.strip().split(',')
            data.append((city, float(latitude), float(longitude)))
    return data

def build_kdb_tree(data, depth=0):
    if not data:
        return None

    axis = depth % 2  # Alternating between latitude and longitude
    data.sort(key=lambda x: x[axis])

    median = len(data) // 2
    node = Node(*data[median])
    node.left = build_kdb_tree(data[:median], depth + 1)
    node.right = build_kdb_tree(data[median + 1:], depth + 1)

    return node

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio medio de la Tierra en kilómetros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def adjust_longitude_distance(latitude):
    # Ajustar la distancia entre líneas de longitud en función de la latitud
    equator_circumference = 40075.0  # Circunferencia de la Tierra en el ecuador en kilómetros
    return equator_circumference * math.cos(math.radians(latitude)) / 360.0

def find_nearest_cities(node, target, num_cities=5, depth=0, best_cities=None):
    if best_cities is None:
        best_cities = [{'city': None, 'coordinates': None, 'distance': float('inf')} for _ in range(num_cities)]

    if node is not None:
        axis = depth % 2
        next_branch = None
        opposite_branch = None

        if target[axis] < node.latitude if axis == 0 else target[axis] < node.longitude:
            next_branch = node.left
            opposite_branch = node.right
        else:
            next_branch = node.right
            opposite_branch = node.left

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

    return best_cities  # Devolver la lista de las ciudades más cercanas

# Obtener coordenadas del usuario por consola
user_latitude = float(input("Ingrese la latitud (-90 a 90): "))
user_longitude = float(input("Ingrese la longitud (-180 a 180): "))
user_target_coordinates = (user_latitude, user_longitude)

# Construir el árbol KDB y encontrar las ciudades más cercanas
file_path = r'D:\Proyectos programación\Citys-coordinates-tree\Databases\cleardata.csv'
city_data = read_csv(file_path)
kdb_tree = build_kdb_tree(city_data)

# Encontrar las ciudades más cercanas
nearest_cities = find_nearest_cities(kdb_tree, user_target_coordinates)

# Mostrar las 5 ciudades más cercanas
print("\nLas 5 ciudades más cercanas son:")
for city_info in nearest_cities:
    print(f"Nombre: {city_info['city']}, Coordenadas: {city_info['coordinates']}, Distancia: {city_info['distance']} km")
