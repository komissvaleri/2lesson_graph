
import numpy as np
import matplotlib.pyplot as plt

print('Квадратическая функция y=ax^2+bx+c. Введите параметры.')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

x = np.linspace(-100, 100, 1000)
y = a * x ** 2 + b * x + c

fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()