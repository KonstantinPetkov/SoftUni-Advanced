numbers = [int(x) for x in input().split()]

sum_of_positive = 0
sum_of_negative = 0

for number in numbers:
    if number < 0:
        sum_of_negative += number
    else:
        sum_of_positive += number

print(f"{sum_of_negative}")
print(f"{sum_of_positive}")

if sum_of_positive > abs(sum_of_negative):
    print("The positives are stronger than the negatives")
elif sum_of_positive < abs(sum_of_negative):
    print("The negatives are stronger than the positives")