# Lekcja 10 - Zadanie 16
# Rozwiązanie w NumPy; uruchom: python zadanie_16.py

import numpy as np

np.random.seed(5)
A = np.random.rand(100, 50)
B = np.random.rand(50, 20)
C_np = A @ B
C_loop = np.zeros((A.shape[0], B.shape[1]))
for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            C_loop[i, j] += A[i, k] * B[k, j]
print("Kształt wyniku:", C_np.shape)
print("Wyniki zgodne (allclose):", np.allclose(C_np, C_loop))
print("NumPy jest szybszy, ponieważ obliczenia są wektoryzowane i mogą korzystać z zoptymalizowanych bibliotek BLAS, zamiast wykonywać trzy pętle w interpreterze Pythona.")
