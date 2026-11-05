# Lekcja 10 - Zadanie 17
# Rozwiązanie w NumPy; uruchom: python zadanie_17.py

import numpy as np

np.random.seed(6)
image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
threshold = np.where(image < 128, 0, 255).astype(np.uint8)
negative = 255 - image
padded = np.pad(image, pad_width=10, mode="constant", constant_values=0)
def show_corners(label, arr):
    print(f"{label}: shape={arr.shape}")
    print("Lewy górny (5):", arr[:5, :5].ravel()[:5])
    print("Prawy górny (5):", arr[:5, -5:].ravel()[:5])
    print("Lewy dolny (5):", arr[-5:, :5].ravel()[:5])
    print("Prawy dolny (5):", arr[-5:, -5:].ravel()[:5])
show_corners("Oryginał", image)
show_corners("Progowanie", threshold)
show_corners("Negatyw", negative)
show_corners("Padding", padded)
