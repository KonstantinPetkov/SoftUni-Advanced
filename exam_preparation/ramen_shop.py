from collections import deque

bowls_of_ramen = list(map(int, input().split(", ")))
list_of_customers = list(map(int, input().split(", ")))

bowls = deque(bowls_of_ramen)
customers = deque(list_of_customers)

while True:

    if not bowls or not customers:
        break

    ramen = bowls.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue

    if ramen > customer:
        ramen -= customer
        bowls.append(ramen)
    elif customer > ramen:
        customer -= ramen
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

