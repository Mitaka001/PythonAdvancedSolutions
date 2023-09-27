data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for col in range(cols):
    sum_col_nums = 0
    for row in range(rows):
        sum_col_nums += matrix[row][col]
    print(sum_col_nums)
