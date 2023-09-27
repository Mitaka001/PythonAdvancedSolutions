matrix_size = input().split(", ")
rows = int(matrix_size[0])
cols = int(matrix_size[1])

matrix = []
sum_elements = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    sum_elements += sum(elements)
    matrix.append(elements)


print(sum_elements)
print(matrix)
