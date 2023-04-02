number_of_queries = int(input())

for _ in range(number_of_queries):
    result = -1
    initial_charge, number_of_turns, a, b  = map(int, input().split())

    maximum = number_of_turns
    minimum = 0

    while minimum <= maximum:
        non_charging_turns = (maximum + minimum) // 2

        charging_turns = number_of_turns - non_charging_turns

        if non_charging_turns*a + charging_turns*b < initial_charge:
            result = max(result, non_charging_turns)
            minimum = non_charging_turns + 1
        else:
            maximum = non_charging_turns - 1


    print(result)