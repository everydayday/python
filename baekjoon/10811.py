def reverse(arr, i , j):
    length = j - i + 1
    for m in range(int(length/2)):
        arr[i],arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    


N, M = map(int,input().split())
arr = [i for i in range(N+1)]   # 0 - N-1
for m in range(M):
    i, j = map(int,input().split())
    reverse(arr, i, j)  # 1번째 => 1번 인덱스

print(*arr[1:]) # 출력만 잘해주면 index 상관 없어

### 다른 분거
# f = lambda:map(int,input().split())
# n,m = f();b=[*range(1,n+1)]
# for _ in range(m):i,j=f();b[i-1:j]=b[i-1:j][::-1]
# print(*b)











