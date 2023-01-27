number = int(input())
cars_record = [input() for _ in range(number)]
car_parking = set()
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for record in cars_record:
    command, car_number = record.split(", ")

    if command == COMMAND_IN:
        car_parking.add(car_number)
    elif command == COMMAND_OUT:
        car_parking.remove(car_number)

if car_parking:
    for car in car_parking:
        print(car)
else:
    print("Parking Lot is Empty")