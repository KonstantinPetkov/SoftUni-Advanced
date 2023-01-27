number_of_guests = int(input())
reservation_list = [input() for _ in range(number_of_guests)]
arrived_guests = []

while True:
    data = input()
    if data == "END":
        break

    arrived_guests.append(data)

not_arrived_guests = set(reservation_list).difference(arrived_guests)

print(len(not_arrived_guests))
for guest in sorted(not_arrived_guests):
    print(guest)