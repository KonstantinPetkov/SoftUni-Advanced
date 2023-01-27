number_of_element = int(input())
elements = set()

for element in range(number_of_element):
    all_elements = input().split()
    for elem in all_elements:
        elements.add(elem)

print('\n'.join(elements))