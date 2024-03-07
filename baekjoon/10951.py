# while True:
#     try:
#         a, b = map(int,(input().split()))
#         print(a+b)
#     except:
#         break

import sys

for i in sys.stdin:
    a,b = map(int,i.split())
    print(a+b)


