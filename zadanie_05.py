# Lekcja 10 - Zadanie 05
# Rozwiązanie w NumPy; uruchom: python zadanie_05.py

import numpy as np

np.random.seed(1)
sales = np.random.randint(10, 100, size=(4, 7))
product_means = np.mean(sales, axis=1)
day_means = np.mean(sales, axis=0)
day_totals = np.sum(sales, axis=0)
print("Sprzedaż:\n", sales)
print("Średnie produktów:", np.round(product_means, 2))
print("Średnie dni:", np.round(day_means, 2))
print("Najlepszy dzień (1-7):", np.argmax(day_totals) + 1)
print("Produkt z najniższą średnią (1-4):", np.argmin(product_means) + 1)
