text = input()
occurrences = {}

for symbol in text:
    if symbol not in occurrences:
        occurrences[symbol] = 0

    occurrences[symbol] += 1

sorted_occurrences_dict = sorted(occurrences.items())

for symbol, times in sorted_occurrences_dict:
    print(f"{symbol}: {times} time/s")