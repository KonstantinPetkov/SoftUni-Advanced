number_of_intersection = int(input())

longest_intersection = []

for _ in range(number_of_intersection):
    first_number, second_number = [numbers.split(",") for numbers in input().split("-")]

    first_range = set(range(int(first_number[0]), int(first_number[1]) + 1))
    second_range = set(range(int(second_number[0]), int(second_number[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection


print(f"Longest intersection is [{', '.join(str(n) for n in longest_intersection)}] with length {len(longest_intersection)}")