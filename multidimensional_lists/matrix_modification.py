n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

while True:
    command = input().split()
    if command[0] == "END":
        break

    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if 0 <= row < n and 0 <= col < len(matrix[0]):
        if command[0] == "Add":
            matrix[row][col] += value
        elif command[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(" ".join(map(str, row)))
