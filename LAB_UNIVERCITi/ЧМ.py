
import numpy as np

def compute_LUR(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    R = np.copy(A)

    for j in range(n):
        for i in range(j, n):
            L[i][j] = R[i][j] - np.sum(L[i][:j] * U[:j, j])
            U[i][j] = (R[i][j] - np.sum(L[i][:j] * U[:j, j])) / L[j][j]

        for i in range(j+1, n):
            R[i][j] = R[i][j] - np.sum(L[i][:j] * U[:j, j])

    return L, U, R

def solve_Ly_b(L, y, b):
    n = len(L)
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i][:i] * y[:i])) / L[i][i]
    return y

def solve_Ux_y(U, x, y):
    n = len(U)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.sum(U[i][i+1:] * x[i+1:])) / U[i][i]
    return x

def compute_residual(A, x, b):
    Ax = np.dot(A, x)
    residual = np.linalg.norm(Ax - b)
    return residual

# Пример использования
A = np.array([[4, -1, 2],
              [-1, 5, 0],
              [2, 0, 6]])
b = np.array([1, 2, 3])

L, U, R = compute_LUR(A)

y = np.zeros(len(b))
y = solve_Ly_b(L, y, b)

x = np.zeros(len(b))
x = solve_Ux_y(U, x, y)

residual = compute_residual(A, x, b)

print("Матрица L:")
print(L)
print("Матрица U:")
print(U)
print("Матрица R:")
print(R)
print("Вектор y:")
print(y)
print("Вектор x:")
print(x)
print("Вектор невязки:")
print(residual)
