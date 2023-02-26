n, m = [int(x) for x in input().split()]

matrix = []
matrix_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

move = 0
players_move = 0

for row in range(n):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        col = matrix[row].index('B')
        matrix_position = [row, col]

while players_move < 3:

    command = input()
    if command == 'Finish':
        break

    current_row, current_column = directions[command]

    new_row = matrix_position[0] + current_row
    new_column = matrix_position[1] + current_column

    if not (0 <= new_row < m and 0 <= new_column < n):
        continue

    elif matrix[new_row][new_column] == 'B' or matrix[new_row][new_column] == 'O':
        continue

    matrix[matrix_position[0]][matrix_position[1]] = '-'
    move += 1
    matrix_position = [new_row, new_column]


    if matrix[new_row][new_column] == 'P':
        players_move += 1
    matrix[new_row][new_column] = 'B'

print('Game over!')
print(f'Touched opponents: {players_move} Moves made: {move}')