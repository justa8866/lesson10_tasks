# Lekcja 10 - Zadanie 04
# Rozwiązanie w NumPy; uruchom: python zadanie_04.py

import numpy as np

np.random.seed(0)
a = np.random.randint(1, 51, size=(5, 4))
print("Tablica:\n", a)
print("Shape:", a.shape)
print("Drugi wiersz:", a[1])
print("Trzecia kolumna:", a[:, 2])
print("Element [2, 3] (indeksy od zera):", a[2, 3])
