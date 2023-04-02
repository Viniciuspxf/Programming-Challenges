test_cases = int(input())

for _ in range(test_cases):
    length, number_of_ants = tuple(map(int, input().split()))

    positions = list(map(int, input().split()))

    while (number_of_ants != len(positions)):
        positions +=  list(map(int, input().split()))
    
    latest = 0
    earliest = 0

    for position in positions:

        relative_position = length - position
        
        current_earliest = min(length - position, position)
        earliest = max(current_earliest, earliest)

        current_latest = max(length - position, position)
        latest = max(current_latest, latest)


    print(earliest, latest)

