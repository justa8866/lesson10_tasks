# Lekcja 10 - Zadanie 19
# Rozwiązanie w NumPy; uruchom: python zadanie_19.py

import numpy as np

np.random.seed(7)
x = np.linspace(0, 10, 100)
y = 2 * x**2 - 3 * x + 5 + np.random.randn(100) * 10
X = np.column_stack((np.ones_like(x), x, x**2))
print("Kształt X:", X.shape)
print("Pierwszych 5 wierszy X:\n", np.round(X[:5], 3))
print("Pierwszych 5 wartości y:", np.round(y[:5], 3))
print("Średnia x²:", np.mean(X[:, 2]))
print("Odchylenie standardowe x²:", np.std(X[:, 2]))
