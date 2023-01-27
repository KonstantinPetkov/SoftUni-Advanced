rows, columns = map(int, input().split())
matrix = [[int(element) for element in input().split()] for _ in range(rows)]

max_sum = 0
current_matrix = []

for row in range(rows - 2):
    for col in range(columns - 2):
        first_row = matrix[row][col: col + 3]
        second_row = matrix[row + 1][col: col + 3]
        third_row = matrix[row + 2][col: col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            current_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*current_matrix[row]) for row in range(3)]