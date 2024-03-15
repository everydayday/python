import matplotlib.pyplot as plt

x = list(range(1,101))
square = [i**2 for i in x]
print(x, square)
print(plt.style.available)
plt.style.use("seaborn-v0_8")
plt.style.use("fast")


fig, ax = plt.subplots()
# ax.plot(square,linewidth=5)
ax.scatter(x,square,c=square, cmap = plt.cm.Blues)

ax.set_title('Square')
ax.set_xlabel('X')
ax.set_ylabel('Y')
# ax.tick_params()
# ax.set_xlim(0,20)
# ax.set_ylim(0,20)
ax.ticklabel_format(style ='plain')



plt.show()