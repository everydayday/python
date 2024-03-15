arr = [n for n in range(30)]

for i in range(28):
    arr[int(input())-1] = 100

arr1 = [a  for a in arr if a != 100]
print(arr1[0]+1)
print(arr1[1]+1)





