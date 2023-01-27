number = int(input())

odd_set = set()
even_set = set()

for row in range(1, number + 1):
    sum_of_ascii = sum(ord(letter) for letter in input()) // row

    if sum_of_ascii % 2 == 0:
        even_set.add(sum_of_ascii)
    else:
        odd_set.add(sum_of_ascii)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=", ")
