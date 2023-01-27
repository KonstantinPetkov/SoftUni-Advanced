from _collections import deque

numbers = deque()

map_func = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None
}

num = int(input())

for _ in range(num):
    data_num = [int(x) for x in input().split()]
    map_func[data_num[0]](data_num)

numbers.reverse()

print(*numbers, sep=", ")