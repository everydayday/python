alphabets = list(input())
count = 0
max_str = alphabets[0]
flag = False
for i in alphabets:
    temp_count = alphabets.count(i)
    if temp_count > count:
        count = temp_count
        max_str = i
        flag = False
    elif temp_count == count:
        flag == True

if flag == True:
    print("?")
else:
    print(max_str)


#### 
from collections import Counter
print(Counter("hello world").most_common(1)[0][0]) # 튜플로 온거
    
