# Lekcja 10 - Zadanie 08
# Rozwiązanie w NumPy; uruchom: python zadanie_08.py

import numpy as np

arr = np.arange(1, 13)
a = arr.reshape(3, 4)
print("3x4:\n", a)
print("2x6:\n", arr.reshape(2, 6))
print("4x3:\n", arr.reshape(4, 3))
print("Flatten:", a.flatten())
print("Ravel:", a.ravel())
copy_flat = a.flatten()
view_flat = a.ravel()
copy_flat[0] = 999
print("Po zmianie flatten oryginał bez zmian:", a[0, 0])
view_flat[0] = 888
print("Po zmianie ravel oryginał zmieniony:", a[0, 0])
print("flatten jest kopią:", not np.shares_memory(a, copy_flat))
print("ravel współdzieli pamięć:", np.shares_memory(a, view_flat))
