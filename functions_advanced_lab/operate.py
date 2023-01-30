def operate(operator, *args):

    if operator == '+':
        result = 0
        for num in args:
            result += int(num)
        return result

    elif operator == '-':
        result = 0
        for num in args:
            result -= int(num)
        return result

    elif operator == '*':
        result = 1
        for num in args:
            result *= int(num)
        return result

    elif operator == '/':
        a = args[0]
        b = args[1]
        if a != 0 and b != 0:
            return a / b


print(operate("/", 12, 0))
print(operate("*", 3, 4))