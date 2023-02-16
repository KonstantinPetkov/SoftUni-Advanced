from collections import deque

seats = input().split(', ')
first_sequence = list(map(int, input().split(', ')))
second_sequence = list(map(int, input().split(', ')))

first_deque = deque(first_sequence)
second_deque = deque(second_sequence)

matched_seats = []
rotations = 0

while len(matched_seats) != 3 and rotations != 10:
    first_number = first_deque.popleft()
    second_number = second_deque.pop()
    letters_of_sum_numbers = chr(first_number + second_number)
    rotations += 1
    founded = False
    check_seat = (f'{first_number}{letters_of_sum_numbers}', f'{second_number}{letters_of_sum_numbers}')

    for seat in check_seat:
        if seat in seats:
            matched_seats.append(seat)
            seats.remove(seat)
            founded = True

    if founded:
        continue

    first_deque.append(first_number)
    second_deque.appendleft(second_number)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f'Rotations count: {rotations}')
