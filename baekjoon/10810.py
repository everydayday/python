
N, M = input().split()
N, M = int(N), int(M)

arr = [0] * N

for p in range(M):
    i, j, k = map(int,input().split())
    for q in range(i-1,j): # 번호와 index 확인
        arr[q] = k  # q에다가 k 넣어주기

print(*arr)

        