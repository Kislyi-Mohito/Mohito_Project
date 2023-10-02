from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Создаем пустой график
fig, ax = plt.subplots()

# Инициализируем пустой график
line, = ax.plot([], [], '*')

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
x_values_d, y_values_d = result_damped


def update(frame):
    # Обновляем данные графика
    line.set_data(x_values_d[:frame + 1], y_values_d[:frame + 1])

    # Устанавливаем пределы осей
    ax.set_xlim(min(x_values_d), max(x_values_d))
    ax.set_ylim(min(y_values_d), max(y_values_d))

    # Добавляем подписи осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Добавляем заголовок
    ax.set_title('Анимированный график')

    # Возвращаем график для отображения
    return line,

# Создаем анимацию
animation = FuncAnimation(fig, update, frames=len(x_values), interval=5)

# Выводим анимацию
plt.show()