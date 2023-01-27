from collections import deque

number_of_petrol = int(input())

pump_deque = deque()
#pump_deque = deque([[int(x) for x in input().split()] for _ in range(number_of_petrol)])

tank = 0
index = 0

for pump in range(number_of_petrol):
    first_element, second_element = input().split()
    pump_deque.append([int(first_element), int(second_element)])

pump_deque_copy = pump_deque.copy()

while pump_deque_copy:
    petrol, distance = pump_deque_copy.popleft()

    tank += petrol

    if tank - distance < 0:
        pump_deque.rotate(-1)
        pump_deque_copy = pump_deque.copy()
        tank = 0
        index += 1
    else:
        tank -= distance

print(index)