rows, columns = map(int, input().split())
matrix = [input().split() for _ in range(int(rows))]

number_of_blocks = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        symbol = matrix[row][col]
        if matrix[row][col + 1] == symbol and matrix[row + 1][col] == symbol and matrix[row + 1][col + 1] == symbol:
            number_of_blocks += 1

print(number_of_blocks)