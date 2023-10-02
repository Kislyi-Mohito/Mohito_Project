import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Параметры
w = 1 # Частота осциллятора
B = 0.9  # Амплитуда внешней силы
Ω = 0.9 # Частота внешней силы

# Временной интервал и шаг
t_start = 0
t_end = 35
dt = 0.1

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

# Построение фазового портрета
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values)
plt.xlabel('Позиция (x)')
plt.ylabel('Скорость (y)')
plt.title('Фазовый портрет линейного гармонического осциллятора')
plt.grid(True)
plt.show()
print('x = ', x_values, "y = ", y_values)