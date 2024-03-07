
arr = []
#arr = list(map(int, input().split()))

# sum_x = arr[0] # 총 금액
# many_n = arr[1] # 물건 종류 수
sum_x = int(input())
many_n = int(input())

# print(f"sumx : {sum_x}")
# print(f"many_n : {many_n}")

items = []
for i in range(0, many_n):
    item = list(map(int, input().split()))
    items.append(item[0])         # 짝수:가격 홀수 : 개수
    items.append(item[1])

prices = items[::2]
#print(f"prices : {prices}")
nums = items[1::2]
#print(f"numbs : {nums}")
guess_sum = 0

for price, num in zip(prices, nums):    # 여러 리스트 값 접근할 수 있음
    guess_sum += price * num

if sum_x == guess_sum:
    print("Yes")
else:
    print("No")



############ 다른 분 거 ######
import sys
input = sys.stdin.readline
total = int(input())
for i in range(int(input())):   # 받아들인 갯수만큼 for문 하겠다.
    a, b = map(int,input().split())
    total -= a * b  # good idea
print("Yes" if total == 0 else "No") # good expression  삼항 조건 연산자





