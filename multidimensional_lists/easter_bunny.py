size = int(input())

matrix = []
bunny_position = []
max_eggs = float("-inf")
max_direction = ''
max_eggs_matrix = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(size):
    matrix.append(input().split())

    for col in range(size):
        if matrix[row][col] == "B":
            bunny_position = [row, col]

for direction, move in possible_moves.items():
    eggs = 0
    current_eggs_matrix = []
    row = bunny_position[0] + move[0]
    col = bunny_position[1] + move[1]

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        eggs += int(matrix[row][col])
        current_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and current_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = current_eggs_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)
