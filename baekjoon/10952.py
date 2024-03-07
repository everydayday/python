import sys

arr = []
while True:
    a, b = map(int,(input().split()))
    if a == 0 and b == 0 :
        break
    arr.append([a,b])

for ar in arr:
    print(ar[0] + ar[1])


#### 다른 분거
import sys

while True:
  a, b = map(int, sys.stdin.readline().split())
  if a == b == 0: break # 한줄 할 수 있으면 한 줄 # 같은 값이면 한꺼번에
  print(a + b)  # 꼭 한꺼번에 출력 안 해도 됨. 하나씩 ok

