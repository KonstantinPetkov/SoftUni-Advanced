from collections import deque

parantheses_deque = deque(input())
opened_parantheses = deque()

while parantheses_deque:
    left_parantheses = "{[("
    left_opened = parantheses_deque.popleft()

    if left_opened in left_parantheses:
        opened_parantheses.append(left_opened)
    elif not opened_parantheses:
        print("NO")
        break
    else:
        correct_open_parantheses = opened_parantheses.pop() + left_opened
        if correct_open_parantheses not in "(){}[]":
            print("NO")
            break
else:
    print("YES")