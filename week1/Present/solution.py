number_of_flowers, remaining_days, water = map(int, input().split())

flowers = list(map(int, input().split()))

higher = 10**10
lower = 0

maximum = 0

while lower <= higher:
    mid = (higher + lower) // 2

    segments = [0]*number_of_flowers
    number_of_segments = 0
    total_number_of_segments = 0

    for i in range(number_of_flowers):
        if i - water >= 0:
            number_of_segments -= segments[i - water]

        if (flowers[i] + number_of_segments < mid):
            growth =  mid - flowers[i] - number_of_segments

            segments[i] = growth
            number_of_segments += growth
            total_number_of_segments += growth

    if total_number_of_segments > remaining_days:
        higher = mid - 1
    else:
        maximum = max(maximum, mid)
        lower = mid + 1


print(maximum)
