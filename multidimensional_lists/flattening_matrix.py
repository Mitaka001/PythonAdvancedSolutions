rows = int(input())

flattened_matrix = []

for row in range(rows):
    numbers = [int(el) for el in input().split(", ")]
    for num in numbers:
        flattened_matrix.append(num)

print(flattened_matrix)
