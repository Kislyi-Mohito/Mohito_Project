import numpy as np

def LU_decomposition(A):
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

def solve_Ly_b(L, b):
    n = len(L)
    y = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - np.sum(L[i][:i] * y[:i])) / L[i][i]

    return y

def solve_Ux_y(U, y):
    n = len(U)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.sum(U[i][i+1:] * x[i+1:])) / U[i][i]

    return x

# Пример использования
A = np.array([[2, -1, 3], [4, 1, -1], [3, 5, -2]])
b = np.array([9, 1, 5])

L, U, R = LU_decomposition(A)
y = solve_Ly_b(L, b)
x = solve_Ux_y(U, y)

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