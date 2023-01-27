text = input().split("|")

my_list = []

for string in text[::-1]:
    my_list.extend(string.split())

print(*my_list)