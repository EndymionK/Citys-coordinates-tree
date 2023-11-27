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

def find_nearest_cities(node, target, num_cities=5, depth=0):
    cities = []

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

        next_best = find_nearest_cities(next_branch, target, num_cities, depth + 1)
        cities.extend(next_best)

        if len(cities) < num_cities or opposite_branch is not None:
            distance_to_target = distance(node.latitude, node.longitude, target[0], target[1])
            cities.append({'city': node.city, 'coordinates': (node.latitude, node.longitude), 'distance': distance_to_target})

            opposite_best = find_nearest_cities(opposite_branch, target, num_cities - len(cities), depth + 1)
            cities.extend(opposite_best)

    return cities

def distance(lat1, lon1, lat2, lon2):
    return ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5

# Obtener coordenadas del usuario por consola
user_latitude = float(input("Ingrese la latitud: "))
user_longitude = float(input("Ingrese la longitud: "))
user_target_coordinates = (user_latitude, user_longitude)

# Construir el árbol KDB y encontrar las ciudades más cercanas
file_path = r'C:\Proyectos programación\Citys-coordinates-tree\Databases\cleardata.csv'
city_data = read_csv(file_path)
kdb_tree = build_kdb_tree(city_data)

nearest_cities = find_nearest_cities(kdb_tree, user_target_coordinates)

# Mostrar las 5 ciudades más cercanas
print("\nLas 5 ciudades más cercanas son:")
for city_info in nearest_cities[:5]:
    print(f"Nombre: {city_info['city']}, Coordenadas: {city_info['coordinates']}, Distancia: {city_info['distance']}")
