box_of_clothes = [int(n) for n in input().split()]
capacity_of_rack = int(input())

count_rack = 1
rack_capacity = capacity_of_rack

while box_of_clothes:
    cloth = box_of_clothes.pop()

    if rack_capacity - cloth >= 0:
        rack_capacity -= cloth
    else:
        count_rack += 1
        rack_capacity = capacity_of_rack - cloth

print(count_rack)
