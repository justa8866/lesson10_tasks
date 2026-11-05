# Lekcja 10 - Zadanie 18
# Rozwiązanie w NumPy; uruchom: python zadanie_18.py

import numpy as np

np.random.seed(10)
data = np.random.rand(50, 2) * 100
query = np.array([50.0, 50.0])
distances = np.sqrt(np.sum((data - query) ** 2, axis=1))
nearest = np.argsort(distances)[:5]
print("Indeks | X | Y | Odległość")
for idx in nearest:
    print(f"{idx:6d} | {data[idx, 0]:7.2f} | {data[idx, 1]:7.2f} | {distances[idx]:9.3f}")
