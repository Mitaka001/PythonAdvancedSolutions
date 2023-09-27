data = input().split("|")
matrix = []

for i in range(len(data) -1, -1, -1):
    row = [int(x) for x in data[i].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=" ", end=" ")
