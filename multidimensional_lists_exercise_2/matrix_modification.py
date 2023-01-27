rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    current_command = command.split()
    action, row, col, value = current_command[0], int(current_command[1]), int(current_command[2]), int(current_command[3])

    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
    elif action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

[print(*row) for row in matrix]

