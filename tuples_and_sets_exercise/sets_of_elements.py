n, m = [int(x) for x in input().split()]

first_set = set(int(input()) for a in range(n))
second_set = set(int(input()) for b in range(m))

print(*first_set.intersection(second_set), sep="\n")