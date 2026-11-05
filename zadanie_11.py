# Lekcja 10 - Zadanie 11
# Rozwiązanie w NumPy; uruchom: python zadanie_11.py

import numpy as np

np.random.seed(3)
sales = np.random.randint(50, 200, size=(6, 28))
trend = np.sum(sales[:, -7:], axis=1) - np.sum(sales[:, :7], axis=1)
weekly = np.array([np.sum(sales[:, start:start+7]) for start in (0, 7, 14, 21)])
totals = np.sum(sales, axis=1)
print("Trend per produkt (ostatni tydzień - pierwszy):", trend)
print("Sumy tygodni:", weekly)
print("Najlepszy tydzień (1-4):", np.argmax(weekly) + 1, "suma:", np.max(weekly))
print("Sprzedaż per produkt (█ = 100 sztuk):")
for i, total in enumerate(totals, 1):
    print(f"Produkt {i}: {'█' * (total // 100)} ({total})")
