from collections import deque

food_per_day = int(input())
quantity_of_each_order = deque([int(num) for num in input().split()])

print(max(quantity_of_each_order))

for order in quantity_of_each_order.copy():
    if food_per_day - order >= 0:
        quantity_of_each_order.popleft()
        food_per_day-= order
    else:
        print(f"Orders left: {' '.join([str(i) for i in quantity_of_each_order])}")
        break
else:
    print(f"Orders complete")
