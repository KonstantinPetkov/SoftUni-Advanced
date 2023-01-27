from _collections import deque

kids_name = input().split(' ')
number_leaves_kids = int(input())
counter = 0
my_deque = deque(kids_name)

while len(my_deque) > 1:
    name_of_leaved_kid = my_deque.popleft()
    counter += 1

    if counter == number_leaves_kids:
        print(f"Removed {name_of_leaved_kid}")
        counter = 0
    else:
        my_deque.append(name_of_leaved_kid)

print(f"Last is {my_deque[0]}")