import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        file = open(f"files/{info[0]}", "w")
        file.close()

    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r") as file:
                text = file.readlines()

            for index in range(len(text)):
                text[index] = text[index].replace(info[1], index[2])

            with open(f"files/{info[0]}", "w") as file:
                file.write("".join(text))

        except FileNotFoundError:
            print("An error occured!")

    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occured!")
    elif command == "End":
        break

