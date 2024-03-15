N, M = map(int,input().split())
arr = [n for n in range(N+1)]
print(arr)
for m in range(M):
    i, j = map(int,input().split())
    arr[i+1],arr[j+1] = arr[j+1],arr[i+1]

print(" ".join(map(str,arr[1:])))









