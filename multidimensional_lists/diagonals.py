size = int(input())

matrix = []

for _ in range(size):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

diagonals = []
second_diagonals = []

for row_index in range(size):
    diagonals.append(matrix[row_index][row_index])

sum_diagonals = sum(diagonals)

for row in range(size):
    second_diagonals.append(matrix[row][size - row - 1])

second_sum = sum(second_diagonals)

print(f"Primary diagonal: {', '.join([str(x) for x in diagonals])}. Sum: {sum_diagonals}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diagonals])}. Sum: {second_sum}")


# second solution
# n = int(input())
# matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
#
# primary_diagonal = [matrix[i][i] for i in range(n)]
# secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(second_diagonals)}")
