original_string = input()
ocurrences = dict()
even_characters = list()
odd_characters = list()

for character in original_string:
    if not character in ocurrences:
        ocurrences[character] = 1
    else:
        ocurrences[character] += 1

for character in ocurrences.keys():
    if ocurrences[character] % 2 == 0:
        even_characters.append(character)
    else:
        odd_characters.append(character)

if len(odd_characters) > 1:
    print("NO SOLUTION")
else:
    for character in even_characters:
        print((ocurrences[character] // 2)*character, end='')
    
    if len(odd_characters) == 1:
        character = odd_characters[0]
        print(ocurrences[character]*character, end='')

    for character in even_characters[::-1]:
        print((ocurrences[character] // 2)*character, end='')
