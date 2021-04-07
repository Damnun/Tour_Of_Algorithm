import heapq
from random import random
hq = []
for i in range(0, 10):
    rand1 = int(random() * 10)
    rand2 = int(random() * 10)
    heapq.heappush(hq, (rand1, rand2))
    print("그냥 heap queue 배열을 출력할 때")
    print(hq)
    print("heap queue를 순차적으로 pop할 때")
while hq:
    print(heapq.heappop(hq))
