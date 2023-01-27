numbers = tuple(map(float, input().split()))
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1

for key, value in counter.items():
    print(f"{key} - {value} times")