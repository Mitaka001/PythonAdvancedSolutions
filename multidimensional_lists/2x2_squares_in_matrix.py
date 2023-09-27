data = input().split()
rows = int(data[0])
cols = int(data[1])

matrix = [[x for x in input().split()] for _ in range(rows)]

matrix_counter = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]
        if current_element == next_element and current_element == element_below and current_element == element_diagonal:
            matrix_counter += 1

print(matrix_counter)
