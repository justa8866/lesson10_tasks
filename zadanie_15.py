# Lekcja 10 - Zadanie 15
# Rozwiązanie w NumPy; uruchom: python zadanie_15.py

import numpy as np

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
kernel = np.array([0.2, 0.6, 0.2])
result = np.empty(len(signal) - len(kernel) + 1)
for i in range(len(result)):
    result[i] = np.sum(signal[i:i+len(kernel)] * kernel)
print("Sygnał oryginalny:", signal)
print("Sygnał wygładzony:", np.round(result, 2))
print("Oryginał (█ = 1):")
for i, value in enumerate(signal):
    print(f"{i:2}: {'█' * int(round(value))} ({value:.1f})")
print("Po wygładzeniu (█ = 1):")
for i, value in enumerate(result):
    print(f"{i:2}: {'█' * int(round(value))} ({value:.1f})")
