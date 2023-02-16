def words_sorting(*data):
    words = {}
    result = []

    for word in data:
        if word not in words:
            words[word] = 0
        words[word] += sum([ord(x) for x in word])

    total_sum = sum(words.values())

    if total_sum % 2 != 0:
        sorted_data = sorted(words.items(), key=lambda x: -x[1])
        for w, v in sorted_data:
            result.append(f"{w} - {v}")
    else:
        for w in sorted(words):
            result.append(f"{w} - {words[w]}")

    return '\n'.join(result)



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
