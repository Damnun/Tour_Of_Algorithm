import heapq as hq

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) # 루트 노드(최솟값)을 pop
    else:
        hq.heappush(a, n) # 힙의 형태로 알아서 넣어줌