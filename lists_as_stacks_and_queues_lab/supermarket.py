from _collections import deque

my_deque = deque()

while True:
    command = input()

    if command == "Paid":
        while my_deque:
            print(my_deque.popleft())
    elif command == "End":
        print(f"{len(my_deque)} people remaining.")
        break
    else:
        my_deque.append(command)
