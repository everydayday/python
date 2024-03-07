N = int(input())
arr1 = list(map(int,input().split()))
card_nums = {}
for k in arr1:
    card_nums[k] = 1

M = int(input())
arr2 = list(map(int,input().split()))
for k in arr2:
    try:
        if card_nums[k] == 1:
            print(1, end=' ')
            
    except :
        print(0, end = ' ')


#### 교수님 푸신법
lst = input().split()

# '6' in db  # 있는지 확인 법





