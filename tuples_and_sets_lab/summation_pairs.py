numbers = list(map(int, input().split()))
target_number = int(input())
targets = set()
mapping = {}

for number in numbers:
    if number in targets:
        targets.remove(number)
        pair = mapping[number]
        del mapping[number]
        print(f'{pair} + {number} = {target_number}')
    else:
        result = target_number - number
        targets.add(result)
        mapping[result] = number



