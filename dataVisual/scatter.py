import matplotlib.pyplot as plt
import random

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(100, 200) for _ in range(100)]

x_walk = [5, 0]
y_walk = [5, -5]


fig, ax = plt.subplots()

x, y = 0, 0
x_data, y_data = [], []
x_data.append(x)
y_data.append(y)



ax.scatter(x,y)
ax.plot(x,y)
ax.scatter(x[:50],y[:50],c='red')
ax.scatter(x[50:],y[50:],c='blue')
plt.show()