number_of_integers, number_of_subarrays = map(int, input().split())
integers = list(map(int, input().split()))

minimum_sum = max(integers)
maximum_sum = sum(integers)

while minimum_sum < maximum_sum:

    middle = (minimum_sum + maximum_sum) // 2
    subarray_counter = 1
    current_sum = 0

    for integer in integers:
        if current_sum + integer > middle:
            subarray_counter += 1
            current_sum = integer
        else:
            current_sum += integer


    if subarray_counter <= number_of_subarrays:
        maximum_sum = middle
    else:
        minimum_sum = middle + 1

print(minimum_sum)
