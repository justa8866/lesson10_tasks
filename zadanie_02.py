# Lekcja 10 - Zadanie 02
# Rozwiązanie w NumPy; uruchom: python zadanie_02.py

import numpy as np

before = np.array([100, 250, 75, 320, 180, 450, 90])
after = np.array([80, 200, 60, 280, 150, 400, 75])
savings = before - after
discounts = savings / before * 100
print("Oszczędności:", np.round(savings, 2))
print("Rabat [%]:", np.round(discounts, 2))
print("Średnia oszczędność:", round(float(np.mean(savings)), 2))
