import sys

number_of_queries = int(input())

for _ in range(number_of_queries):
    number_of_piles = int(input())
    piles = list(map(int, input().split()))

    maximum = number_of_piles - 1
    minimum = 0

    while minimum <= maximum:
        middle = (maximum + minimum) // 2

        print("?", middle + 1 - minimum, end=" ")

        for index in range(minimum, middle + 1):
            print(index + 1, end=" ")
        print()

        sys.stdout.flush()

        current_sum = int(input())

        if sum(piles[minimum:middle + 1]) == current_sum:
            minimum = middle + 1
        else:
            maximum = middle - 1

    print("!", minimum + 1)
    sys.stdout.flush()
