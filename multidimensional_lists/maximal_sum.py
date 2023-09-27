data = input().split()
rows = int(data[0])
cols = int(data[1])

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

biggest_sum = float("-inf")
max_sum_matrix = []

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_square_sum = sum([
            matrix[row_index][col_index], matrix[row_index][col_index + 1], matrix[row_index][col_index + 2],
            matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1], matrix[row_index + 1][col_index + 2],
            matrix[row_index + 2][col_index], matrix[row_index + 2][col_index + 1], matrix[row_index + 2][col_index + 2]
        ])

        if current_square_sum > biggest_sum:
            biggest_sum = current_square_sum
            max_sum_matrix = [
                matrix[row_index][col_index:col_index + 3],
                matrix[row_index + 1][col_index:col_index + 3],
                matrix[row_index + 2][col_index:col_index + 3]
            ]

print(f"Sum = {biggest_sum}")
for row in max_sum_matrix:
    print(" ".join(map(str, row)))


# second solution
# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# max_sum = float("- inf")
# max_row = 0
# max_col = 0
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_sum = 0
#         for r in range(row, row + 3):
#             for c in range(col, col + 3):
#                 current_sum += matrix[r][c]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_row = row
#             max_col = col
# print(f"Sum = {max_sum}")