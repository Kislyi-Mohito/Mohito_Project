import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Параметры
w = 5  # Частота осциллятора
B = 0.2  # Амплитуда внешней силы
Ω = 0.8  # Частота внешней силы

# Временной интервал
t_start = 0
t_end = 70
dt = 0.01

# Функция, описывающая систему дифференциальных уравнений
def harmonic_oscillator(state, t):
    x, y = state
    dxdt = y
    dydt = -w**2 * x + B * np.cos(Ω * t)
    return [dxdt, dydt]

# Начальные условия
initial_state = [1.0, 0.0]  # Начальная позиция и скорость

# Решение дифференциальных уравнений
t_values = np.arange(t_start, t_end, dt)
result = np.vstack(odeint(harmonic_oscillator, initial_state, t_values)).T

# Извлечение результатов
x_values, y_values = result


# Параметры затухания
gamma = 0.1  # Коэффициент затухания

# Функция, описывающая систему дифференциальных уравнений с затуханием
def damped_harmonic_oscillator(state, t):
    x, y = state
    dxdt = y
    dydt = -w**2 * x - gamma * y + B * np.cos(Ω * t)
    return [dxdt, dydt]

# Решение дифференциальных уравнений с затуханием
result_damped = np.vstack(odeint(damped_harmonic_oscillator, initial_state, t_values)).T

# Извлечение результатов с затуханием
x_values_damped, y_values_damped = result_damped

# Построение фазового портрета с затуханием
plt.figure(figsize=(10, 5))
plt.plot(x_values_damped, y_values_damped)
plt.xlabel('Позиция (x)')
plt.ylabel('Скорость (y)')
plt.title('Фазовый портрет линейного гармонического осциллятора с затуханием')
plt.grid(True)
plt.show()
