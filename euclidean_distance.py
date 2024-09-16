import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktalar listesi
points = [(1, 2), (4, 6), (5, 8), (7, 1)]

# Mesafeleri tutmak için boş liste
distances = []

# Tüm nokta çiftleri arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul ve yaz
min_distance = min(distances)
print("Minimum mesafe:", min_distance)

