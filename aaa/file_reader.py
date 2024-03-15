# with open("pythonchap\pi_digits.txt", encoding='utf-8') as file:
#     for line in file:
#         print(line.rstrip())


# import csv

# with open("pythonchap/grades.csv") as file:
#     reader = csv.reader(file, delimiter=',')
#     for line in reader:
#         print(line)


# for i in range(5):
#     print(i)

import os
from pathlib import Path


path = Path('./aaa/aaa/aa.txt')

# with open(path,'w') as file:
#     file.write("sfsfsf\n")

try :
    with open(path) as file:
        for line in file:
            print(line)
except Exception as e:
    print(e)


import json
# print(json.dump(['foo', {'bar':('bar',None)}]))

data1 = json.parse("{'a':1, 'b':2}")
print(type(data1))




