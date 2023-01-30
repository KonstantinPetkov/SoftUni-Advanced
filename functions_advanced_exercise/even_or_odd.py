def even_odd(*args):
     result = []
     command = args[-1]

     for number in args[:-1]:
         if int(number) % 2 == 0 and command == "even":
             result.append(number)
         elif int(number) % 2 != 0 and command == "odd":
             result.append(number)

     return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))