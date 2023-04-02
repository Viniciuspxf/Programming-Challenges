number_of_cases = int(input())

for _ in range(number_of_cases):
    string_length = int(input())
    current_string = input()
    
    minimum = 1

    for character in current_string:
        character_order = ord(character) - ord('a') + 1
        minimum = character_order if character_order > minimum else minimum
    
    print(minimum)

