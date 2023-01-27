number = int(input())
usernames = set()

for _ in range(number):
    usernames.add(input())

print('\n'.join(usernames))