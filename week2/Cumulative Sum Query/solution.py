number_of_integers = int(input())

sum_array = []

integers = list(map(int, input().split()))

sum_array.append(integers[0])

for i in range(1, number_of_integers):
    sum_array.append(integers[i] + sum_array[i-1])

number_of_queries = int(input())

for _ in range(number_of_queries):
    i, j = map(int, input().split())
    
    result = sum_array[j] - (sum_array[i - 1] if i - 1 >= 0 else 0)
    print(result)
