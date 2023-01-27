first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
number = int(input())

for n in range(number):
    command, *data = input().split()
    current_command = command + " " + data.pop(0)

    if current_command == "Add First":
        [first_set.add(int(element)) for element in data]
    elif current_command == "Add Second":
        [second_set.add(int(element)) for element in data]
    elif current_command == "Remove First":
        [first_set.discard(int(element)) for element in data]
    elif current_command == "Remove Second":
        [second_set.discard(int(element)) for element in data]
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
