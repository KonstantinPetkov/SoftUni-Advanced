from _collections import deque

quantity_of_water = int(input())

queue = deque()
while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input()
    if command == "End":
        break

    if "refill" in command:
        splitted_command = command.split(' ')
        refill_litters = int(splitted_command[1])
        quantity_of_water += refill_litters
    else:
        liters = int(command)
        if liters <= quantity_of_water:
            print(f"{queue.popleft()} got water")
            quantity_of_water -= liters
        else:
            print(f"{queue.popleft()} must wait")

print(f"{quantity_of_water} liters left")