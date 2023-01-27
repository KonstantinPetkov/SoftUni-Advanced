from collections import deque
from datetime import datetime, timedelta

robots_dict = {}
robot = input().split(";")

for r in robot:
    name, time_needed = r.split("-")
    robots_dict[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots_dict.items():
        if value[1] != 0:
            robots_dict[name][1] -= 1

    for name, value in robots_dict.items():
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots_dict[robot_name][1] = data[0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")

