data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)

biggest_sum = float("-inf")
max_sum_matrix = []

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        next_element_below = matrix[row_index + 1][col_index + 1]
        result = current_element + next_element + element_below + next_element_below
        if result > biggest_sum:
            biggest_sum = result
            max_sum_matrix = [
                [current_element, next_element],
                [element_below, next_element_below]
            ]

for el in max_sum_matrix:
    print(*el)
print(biggest_sum)
