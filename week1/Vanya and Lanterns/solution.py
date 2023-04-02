number_of_lanterns, street_length = map(int, input().split())

lanterns = list(map(int, input().split()))

lanterns.sort()

radius = max(lanterns[0], street_length - lanterns[-1])

for index in range(1, len(lanterns)):
    current_radius = (lanterns[index] - lanterns[index - 1])/ 2
    radius = max(radius, current_radius)

print(radius)