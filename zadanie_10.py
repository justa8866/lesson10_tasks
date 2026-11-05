# Lekcja 10 - Zadanie 10
# Rozwiązanie w NumPy; uruchom: python zadanie_10.py

import numpy as np

exams = np.array([[78, 85, 92, 88], [65, 72, 68, 70], [90, 88, 95, 92], [55, 60, 58, 62], [82, 79, 85, 80]])
bonus = np.array([5, 10, 5, 10])
multipliers = np.array([1.0, 1.1, 0.95, 1.15, 1.0])[:, np.newaxis]
with_bonus = exams + bonus
result = with_bonus * multipliers
print("Przed:\n", exams)
print("Po bonusie:\n", with_bonus)
print("Po bonusie i mnożniku:\n", np.round(result, 2))
