# Вариант 10

import random
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import animation
import csv


def animated(n):
    ax_anm.clear()
    ax_anm.plot(Set[0, :n + 1], Set[1, :n + 1], c='orange')
    ax_anm.scatter(Set[0, n], Set[1, n], c='orange', marker='o')
    ax_anm.set_xlim([0, np.pi * 4])
    ax_anm.set_ylim([-1.05, 1.05])


# Задание 1. Убедиться, что NumPy быстрее работает с массивами

array_1 = [random.randint(1, 100) for i in range(10 ^ 6)]
array_2 = [random.randint(1, 100) for i in range(10 ^ 6)]
output = []

start_1 = time.perf_counter()
for i in range(len(array_1)):
    array_1[i] *= array_2[i]
end_time_1 = time.perf_counter() - start_1

array_1 = np.random.randint(1, 100, 10 ^ 6)
array_2 = np.random.randint(1, 100, 10 ^ 6)
start_2 = time.perf_counter()
output = np.multiply(array_1, array_2)
end_time_2 = time.perf_counter() - start_2

print(end_time_1, ' - время перемножения обычных списков')
print(end_time_2, ' - время перемножения массивов NymPy ')

# Задание 2. Построение гистограмм

raw = []
normalized = []
column = 5
with open("data2.csv", 'r') as csvfile:
    csvfile.readline()
    lines = csv.reader(csvfile, delimiter=',')
    for line in lines:
        if line[column] != '':
            normalized.append(float(line[column]))
            raw.append(float(line[column]))

# Гистограмма
bins = 20
fig1, ax1 = plt.subplots()
ax1.set_title('Гистограмма')
ax1.set_xlabel('Sulfate')
ax1.set_ylabel('Частота')
ax1.hist(raw, bins, density=True, color='purple', edgecolor='black')
plt.show()

# Нормализованная гистограмма
fig2, ax2 = plt.subplots()
ax2.set_title('Нормализованная гистограмма')
ax2.set_xlabel('Sulfate')
ax2.set_ylabel('Частота')
ax2.hist(normalized, bins, density=True, color='lightblue', edgecolor='black')
plt.show()

# Среднеквадратичное отклонение
avr_dev = np.std(normalized)
print('Среднеквадратичное отклонение = ' + str(avr_dev))

# Задание №3. Построение трёхмерного графика
x = np.linspace(-np.pi * 3, np.pi * 3, 100)
y = x * np.cos(x)
z = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()

# Дополнительное задание

t = np.linspace(0, 20, 100)
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

Set = np.array([x, y])
points = len(t)
fig = plt.figure()
ax_anm = plt.axes()
line_anm = animation.FuncAnimation(fig, animated, interval=100, frames=points)
plt.show()