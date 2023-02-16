from collections import deque

eggs_size = list(map(int, input().split(", ")))
size_paper = list(map(int, input().split(", ")))

eggs = deque(eggs_size)
papers = deque(size_paper)

box = 50
filled_box = 0

while True:

    if not eggs or not papers:
        break

    egg = eggs.popleft()

    if egg <= 0:
        continue

    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    paper = papers.pop()
    wrapped_egg = egg + paper

    if wrapped_egg <= box:
        filled_box += 1

if filled_box:
    print(f"Great! You filled {filled_box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")

if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")