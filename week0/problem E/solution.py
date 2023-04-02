test_cases = int(input())

for _ in range(test_cases):
    length, number_of_queries = tuple(map(int, input().split()))
    even_numbers_counter = 0
    odd_numbers_counter = 0
    sum = 0

    number_list = map(int, input().split())

    for current_number in number_list:
        sum += current_number
        
        if current_number % 2 == 0:
            even_numbers_counter += 1
        else:
            odd_numbers_counter += 1

    for b in range(number_of_queries):
        query_type, current_number = tuple(map(int , input().split()))

        if query_type == 0:
            sum += even_numbers_counter*current_number

            if current_number % 2 == 1:
                odd_numbers_counter += even_numbers_counter
                even_numbers_counter = 0

        else: 
            sum += odd_numbers_counter*current_number

            if current_number % 2 == 1:
                even_numbers_counter += odd_numbers_counter
                odd_numbers_counter = 0

        print(sum)
