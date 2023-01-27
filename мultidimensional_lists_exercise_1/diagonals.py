number_of_rows = int(input())
matrix = [[int(element) for element in input().split(", ")] for _ in range(number_of_rows)]
primery_diagonal = [matrix[i][i] for i in range(number_of_rows)]
secondary_diagonal = [matrix[i][number_of_rows - i - 1] for i in range(number_of_rows - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primery_diagonal)}. Sum: {sum(primery_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal][::-1])}. Sum: {sum(secondary_diagonal)}")