matrix = []
my_position = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
target_position = []
targets = 0


for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]

        elif matrix[row][col] == "x":
            targets += 1

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == "shoot":
        r = my_position[0] + possible_moves[command[1]][0]
        c = my_position[1] + possible_moves[command[1]][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                target_position.append([r, c])
                break

            r += possible_moves[command[1]][0]
            c += possible_moves[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(target_position)} targets hit.")
            break

    elif command[0] == "move":
        steps = int(command[2])
        direction = command[1]

        if direction == "up":
            r = my_position[0] - steps
            c = my_position[1]

        elif direction == "down":
            r = my_position[0] + steps
            c = my_position[1]

        elif direction == "right":
            r = my_position[0]
            c = my_position[1] + steps

        else:
            r = my_position[0]
            c = my_position[1] - steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in target_position]
