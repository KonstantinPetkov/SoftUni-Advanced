number = int(input())
matrix = [[int(element) for element in input().split()] for _ in range(number)]

sum_of_primery_diagonal = sum([matrix[i][i] for i in range(number)])
sum_of_secondary_diagonal = sum([matrix[i][number - i - 1] for i in range(number - 1, -1, -1)])
difference = abs(sum_of_primery_diagonal - sum_of_secondary_diagonal)

print(difference)

