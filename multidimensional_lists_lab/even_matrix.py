rows = int(input())
matrix = []

for _ in range(rows):
    current_row = [int(element) for element in input().split(", ") if int(element) % 2 == 0]
    matrix.append(current_row)

print(matrix)