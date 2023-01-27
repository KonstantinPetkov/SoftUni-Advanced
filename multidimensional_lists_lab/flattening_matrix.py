number_of_rows = int(input())
matrix = [[int(element) for element in input().split(", ")] for _ in range(number_of_rows)]
result = [number for row in matrix for number in row]
print(result)
