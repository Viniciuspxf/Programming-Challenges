number_of_socks = int(input())

socks = list(map(int, input().split()))
sum = 0

socks_dictionary = dict()

for sock in socks:

    if sock in socks_dictionary:
        socks_dictionary[sock] += 1
    else:
        socks_dictionary[sock] = 1


for socks in socks_dictionary.values():
    pairs = socks // 2
    
    sum += pairs

print(sum)