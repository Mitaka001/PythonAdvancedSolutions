size = int(input())

matrix = []

for _ in range(size):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][- i - 1] for i in range(size)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
