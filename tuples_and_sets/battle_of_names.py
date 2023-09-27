n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name_sum = sum([ord(element) for element in input()]) // i

    if name_sum % 2 == 0:
        even_set.add(name_sum)

    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    result = odd_set | even_set

elif sum(odd_set) > sum(even_set):
    result = odd_set - even_set

else:
    result = odd_set ^ even_set

print(*result, sep=', ')
