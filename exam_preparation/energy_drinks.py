from collections import deque

caffeinе = list(map(int, input().split(', ')))
drinks = list(map(int, input().split(', ')))

caffeine_deque = deque(caffeinе)
drinks_deque = deque(drinks)

current_coffeine = 0

while True:

    if not caffeine_deque or not drinks_deque:
        break

    caffeine = caffeine_deque.pop()
    drink = drinks_deque.popleft()
    sum_of_caffeine = caffeine * drink

    if sum_of_caffeine + current_coffeine <= 300:
        current_coffeine += sum_of_caffeine
        continue
    else:
        drinks_deque.append(drink)
        current_coffeine -= 30
        if current_coffeine < 0:
            current_coffeine = 0

if drinks_deque:
    print(f"Drinks left: {', '.join(str(x) for x in drinks_deque)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_coffeine} mg caffeine.")