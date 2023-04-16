number_of_integers, number_of_operations, number_of_queries = map(int, input().split())

integers = list(map(int, input().split()))
sum_array = [0]*number_of_integers
operations = []
multipliers = [0]*number_of_operations

for _ in range(number_of_operations):
    left, right, value = map(int, input().split())
    operations.append((left, right, value))

for _ in range(number_of_queries):
    left, right = map(int, input().split())

    multipliers[left - 1] += 1

    if right < number_of_operations:
        multipliers[right] -= 1

for i in range(1, len(multipliers)):
    multipliers[i] += multipliers[i - 1]


for i in range(number_of_operations):
    left, right, value = operations[i]

    sum_array[left - 1] += value*multipliers[i]

    if right < number_of_integers:
        sum_array[right] -= value*multipliers[i]

for i in range(1, len(sum_array)):
    sum_array[i] += sum_array[i - 1]

for i in range(number_of_integers):
    print(sum_array[i] + integers[i], end = " ")