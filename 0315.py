


# with open ('a.csv') as f:
#     for line in f:
#         print(line.rstrip().split(sep=','))
# 이름 안에 , 가 있어서 제대로 안 잘리는 문제점 있었음

import os
# os.path
from pathlib import Path


import csv

from matplotlib import pyplot as plt

import datetime
from datetime import datetime 

x1, y1 = [], []
x2, y2 = [], []

new_var = 2
COL_TMAX = 2


with open(Path('b.csv')) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:        
        x1.append(line[new_var])        
        x2.append(line[COL_TMAX])
        y1.append(line[new_var])
        y2.append(line[5])
# for idx, h in enumerate(header):
#     print(idx, h)


plt.xticks(rotation = 90)
plt.title("TMAX")

plt.plot(x1, y1, label = "TMAX")
plt.plot(x2, y2, label = "TMIN")
plt.fill_between(x1,y1,y2, alpha = 0.2)
plt.legend()





plt.show()




