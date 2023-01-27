rows = int(input())

matrix = []
position_of_bunny = []
best_path = []

best_direction = None
max_collected_eggs = 0

direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        position_of_bunny = [row, matrix[row].index('B')]

for direction, positions in direction.items():
    row, col = [
        position_of_bunny[0] + positions[0],
        position_of_bunny[1] + positions[1]
    ]
    path = []
    collected_eggs = 0

    while 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)