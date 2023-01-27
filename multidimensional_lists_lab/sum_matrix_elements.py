number_of_rows, number_of_columns = map(int, input().split(", "))
matrix = []
sum_of_elements = 0

for row in range(number_of_rows):
    row_data = list(map(int, input().split(", ")))
    matrix.append(row_data)

for i in range(len(matrix)):
    current_row = matrix[i]
    sum_of_elements += sum(current_row)

print(sum_of_elements)
print(matrix)