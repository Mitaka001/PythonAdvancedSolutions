size = int(input())

matrix = []

for _ in range(size):
    elements = [x for x in input()]
    matrix.append(elements)

symbol = input()
position = None

for row_index in range(size):
    if position:
        break
    for col_index in range(len(matrix[row_index])):
        current_symbol = matrix[row_index][col_index]
        if current_symbol == symbol:
            position = (row_index, col_index)
            print(position)
            break
if not position:
    print(f"{symbol} does not occur in the matrix")
