from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Создаем пустой график
fig, ax = plt.subplots()

# Инициализируем пустой график
line, = ax.plot([], [], '-')

# Параметры
w = 1  # Частота осциллятора
B = 0.9  # Амплитуда внешней силы
Ω = 0.9  # Частота внешней силы

# Временной интервал и шаг
t_start = 0
t_end = 35
dt = 0.1


# Функция, описывающая систему дифференциальных уравнений
def harmonic_oscillator(state, t):
    x, y = state
    dxdt = y
    dydt = -w ** 2 * x + B * np.cos(Ω * t)
    return [dxdt, dydt]


# Начальные условия
initial_state = [1.0, 0.0]  # Начальная позиция и скорость

# Решение дифференциальных уравнений
t_values = np.arange(t_start, t_end, dt)
result = np.vstack(odeint(harmonic_oscillator, initial_state, t_values)).T

# Извлечение результатов
x_values, y_values = result

# Устанавливаем пределы осей
ax.set_xlim(min(x_values), max(x_values))
ax.set_ylim(min(y_values), max(y_values))

# Добавляем подписи осей
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Добавляем заголовок
ax.set_title('Анимированный график')


# Функция обновления кадра
def update(frame):
    # Обновляем данные графика
    line.set_data(x_values[:frame + 1], y_values[:frame + 1])
    return line,


# Создаем анимацию
animation = FuncAnimation(fig, update, frames=len(x_values), interval=1)

# Выводим анимацию
plt.show()
