# Lekcja 10 - Zadanie 09
# Rozwiązanie w NumPy; uruchom: python zadanie_09.py

import numpy as np

np.random.seed(2)
scores = np.random.randint(40, 100, size=(20, 3))
minimum = np.min(scores, axis=0)
maximum = np.max(scores, axis=0)
normalized = (scores - minimum) / (maximum - minimum)
print("Oceny:\n", scores)
print("Po normalizacji Min-Max:\n", np.round(normalized, 3))
print("Minimum kolumn:", np.min(normalized, axis=0))
print("Maksimum kolumn:", np.max(normalized, axis=0))
for j in range(scores.shape[1]):
    print(f"\nPrzed normalizacją, przedmiot {j+1}:")
    counts, edges = np.histogram(scores[:, j], bins=5, range=(40, 100))
    for i, count in enumerate(counts):
        print(f"{edges[i]:5.1f}-{edges[i+1]:5.1f}: {'█' * count} ({count})")
    print(f"Po normalizacji, przedmiot {j+1}:")
    counts, edges = np.histogram(normalized[:, j], bins=5, range=(0, 1))
    for i, count in enumerate(counts):
        print(f"{edges[i]:.1f}-{edges[i+1]:.1f}: {'█' * count} ({count})")
