rows = int(input())
square_matrix = []
is_find = False

for row in range(rows):
    row_data = list(input())
    square_matrix.append(row_data)

special_symbol = input()

for row in range(len(square_matrix)):
    for col in range(len(square_matrix[row])):
        element = square_matrix[row][col]
        if element == special_symbol:
            print(f"({row}, {col})")
            is_find = True
            break

if not is_find:
    print(f"{special_symbol} does not occur in the matrix")

