size = int(input())

matrix = []

for _ in range(size):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

sum_nums = 0

for row_index in range(size):
    sum_nums += matrix[row_index][row_index]


print(sum_nums)
