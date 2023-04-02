number_of_cases = int(input())

for _ in range(number_of_cases):
    a, b = tuple(input().split())
    print(int(a) + int(b))