arr = []

for i in range(9):
    arr.append(int(input()))

max_num = max(arr)

index = arr.index(max_num)

print(max_num)
print(index + 1)

