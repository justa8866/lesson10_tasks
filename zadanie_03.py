# Lekcja 10 - Zadanie 03
# Rozwiązanie w NumPy; uruchom: python zadanie_03.py

import numpy as np

temps = np.array([15, 18, 22, 25, 23, 20, 17, 14, 16, 19, 21, 24])
print("Indeksy parzyste:", temps[::2])
print("Ostatnie 5:", temps[-5:])
print("Odwrócona kolejność:", temps[::-1])
print("Powyżej 20:", temps[temps > 20])
