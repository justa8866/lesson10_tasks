# Lekcja 10 - Zadanie 14
# Rozwiązanie w NumPy; uruchom: python zadanie_14.py

import numpy as np

coords = np.linspace(-1, 1, 1000)
x, y = np.meshgrid(coords, coords)
inside = x**2 + y**2 <= 1
pi_estimate = 4 * np.sum(inside) / inside.size
print("Oszacowane pi:", pi_estimate)
print("Błąd bezwzględny:", abs(pi_estimate - np.pi))
print("Mapa pierwszych 20x20 punktów (● = w kole, · = poza):")
for row in inside[:20, :20]:
    print("".join(np.where(row, "●", "·")))
