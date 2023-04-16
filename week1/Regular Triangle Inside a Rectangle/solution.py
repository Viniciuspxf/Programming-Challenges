import math

higher = math.pi / 6
lower = 0

A, B = map(int, input().split())
A, B = (min(A,B), max(A,B))

for _ in range(300):
    mid = (lower + higher) / 2

    l = A/math.cos(mid)

    if l*math.cos(math.pi / 6 - mid) <= B:
        lower = mid
    else: 
        higher = mid 


print(l)