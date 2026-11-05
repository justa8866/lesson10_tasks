# Lekcja 10 - Zadanie 12
# Rozwiązanie w NumPy; uruchom: python zadanie_12.py

import numpy as np

point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])
distance = np.sqrt(np.sum((point_a - point_b) ** 2))
print("Odległość A-B:", round(float(distance), 3))
np.random.seed(4)
points = np.random.rand(4, 5)
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
distance_matrix = np.sqrt(np.sum(diff ** 2, axis=2))
print("Macierz odległości 4x4:")
for row in distance_matrix:
    print(" ".join(f"{value:.3f}" for value in row))
