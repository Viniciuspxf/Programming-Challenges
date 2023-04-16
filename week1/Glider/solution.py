number_of_ascending_airflows, altitude = map(int, input().split())

max_distance = 0
current_distance = 0
current_altitude = altitude

ascending_airflows = []

for _ in range(number_of_ascending_airflows):
    x1, x2 = map(int, input().split())
    ascending_airflows.append((x1,x2))

i = j = 0


current_distance += ascending_airflows[j][1] - ascending_airflows[j][0]
j += 1


while i < len(ascending_airflows):

    while j < len(ascending_airflows) and ascending_airflows[j][0] - ascending_airflows[j - 1][1] < current_altitude:
        airflow_size = ascending_airflows[j][1] - ascending_airflows[j][0]
        distance_between_airflows = ascending_airflows[j][0] - ascending_airflows[j - 1][1]
        
        current_distance += airflow_size + distance_between_airflows
        
        current_altitude -= distance_between_airflows
        
        j += 1

    current_distance += current_altitude
    max_distance = max(max_distance, current_distance)

    if i + 1 < len(ascending_airflows):
        airflow_size = ascending_airflows[i][1] - ascending_airflows[i][0]
        distance_between_airflows = ascending_airflows[i + 1][0] - ascending_airflows[i][1]
        
        current_distance -= distance_between_airflows + airflow_size + current_altitude

        current_altitude += distance_between_airflows

    i += 1

print(max_distance)