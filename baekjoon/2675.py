T = int(input())
for _ in range(T):
    arr = list(input().split())
    arr1 = input().split()   
    # str로 받아들이고 필요할 때 int 해주면 됨
    R = int(arr[0])
    S = arr[1]
    
    for index in range(len(S)):    # index 접근
        for i in range(R):          # R번 출력
            print(S[index],end="")

            # print(i * int(n),end="") # for 문 안 하고도 i 번 출력된다
    print() # 줄 바꿈








# 파이썬에서 len함수를 보면
# Return the number of items in a container.
# 라 되어 있는데 container는 무엇을 말하는 거야?