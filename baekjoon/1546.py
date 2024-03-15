N = int(input())
arr = list(map(int,input().split()))
max_num = max(arr)
new_arr = [a/(max_num) * 100 for a in arr]
mysum = sum(arr)
max_num = max(arr)
# for i in new_arr:
#     sum += i
# sum 함수 이용


print(mysum/max_num)


