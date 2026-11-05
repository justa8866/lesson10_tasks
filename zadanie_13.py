# Lekcja 10 - Zadanie 13
# Rozwiązanie w NumPy; uruchom: python zadanie_13.py

import numpy as np

np.random.seed(42)
data = np.concatenate([np.random.randn(100) * 10 + 50, np.array([150, -50, 200, -100, 180])])
np.random.shuffle(data)
def stats(values, label):
    print(f"{label}: n={values.size}, mean={np.mean(values):.2f}, std={np.std(values):.2f}, min={np.min(values):.2f}, max={np.max(values):.2f}")
def histogram(values, label):
    print(label)
    counts, edges = np.histogram(values, bins=10)
    for i, count in enumerate(counts):
        print(f"{edges[i]:7.1f}..{edges[i+1]:7.1f}: {'█' * count} ({count})")
stats(data, "Przed")
z = (data - np.mean(data)) / np.std(data)
mask = np.abs(z) > 3
print("Outliery (|z| > 3):", data[mask])
clean = data[~mask]
z_clean = (clean - np.mean(clean)) / np.std(clean)
stats(clean, "Po usunięciu")
print("Z-score po oczyszczeniu: mean=", round(float(np.mean(z_clean)), 6), "std=", round(float(np.std(z_clean)), 6))
histogram(data, "Histogram przed:")
histogram(clean, "Histogram po:")
