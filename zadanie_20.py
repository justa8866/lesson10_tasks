# Lekcja 10 - Zadanie 20
# Rozwiązanie w NumPy; uruchom: python zadanie_20.py

import numpy as np

np.random.seed(8)
batch = np.random.randn(32, 10) * 5 + 20
mean = np.mean(batch, axis=0)
std = np.std(batch, axis=0)
batch_norm = (batch - mean) / std
gamma, beta = 2.0, 1.0
output = gamma * batch_norm + beta
for name, values in (("Przed", batch), ("Po normalizacji", batch_norm), ("Po scale/shift", output)):
    print(f"{name} - średnie per cecha:", np.round(np.mean(values, axis=0), 3))
    print(f"{name} - std per cecha:", np.round(np.std(values, axis=0), 3))
print("Batch po normalizacji:\n", np.round(batch_norm, 3))
print("Batch po scale/shift:\n", np.round(output, 3))
for label, values in (("Przed", batch[:, 0]), ("Po scale/shift", output[:, 0])):
    print(f"Histogram cechy 0 - {label}:")
    counts, edges = np.histogram(values, bins=8)
    for i, count in enumerate(counts):
        print(f"{edges[i]:7.2f}..{edges[i+1]:7.2f}: {'█' * count} ({count})")
