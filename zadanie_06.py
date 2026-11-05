# Lekcja 10 - Zadanie 06
# Rozwiązanie w NumPy; uruchom: python zadanie_06.py

import numpy as np

grades = np.array([78, 45, 92, 67, 34, 88, 56, 91, 23, 85, 73, 95])
print("Oceny wysokie:", grades[grades >= 80])
print("Oceny niedostateczne:", grades[grades < 50])
print("Liczba ocen [60, 80):", np.sum((grades >= 60) & (grades < 80)))
corrected = grades.copy()
corrected[corrected < 50] = 50
print("Oceny po korekcie:", corrected)
