import numpy as np
import matplotlib.pyplot as plt

# Задання діапазону x
x = np.linspace(0, 5, 1000)

# Обчислення значень функції Y(x)
y = np.sqrt(x) * np.sin(10 * x)

# Побудова графіку
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='Y(x) = sqrt(x) * sin(10x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x)')
plt.grid(True)
plt.legend()
plt.show()
