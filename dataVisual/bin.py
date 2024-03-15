from matplotlib import pyplot as plt


fig, ax = plt.subplots()

names =["Korean","Eng"]

y1 = [50, 30]
y2 = [70, 50]
y3 = [20, 70]

ax.plot(names, y1, color="red", label = "Hong")
ax.plot(names, y2, color="blue", label = "Lee")
ax.plot(names, y3, color="orange", label = "Kang")

plt.show()



