dic = {}
nums = []


for _ in range(10):
    nums.append(int(input()))

for num in nums:
    dic[num% 42] = 1

print(len(dic.keys()))

## 다른 분 꺼
print(len(set([int(input()) % 42 for _ in range(10)])))

# [] 안에 for 문
# set으로 받아들이기
print(len(set([int(input()) for _ in range(10)])))

arr = []
for d in nums:
    if d not in arr:
        arr.append(d)

