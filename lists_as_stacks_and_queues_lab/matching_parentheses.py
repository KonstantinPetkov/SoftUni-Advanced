expression = input()
parentheses = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses.append(i)
    elif expression[i] == ")":
        first_index = parentheses.pop()

        print(expression[first_index: i + 1])

