def age_assignment(*names, **data):
    result = []

    for letter, age in data.items():
        name = ""

        for current_name in names:
            if current_name.startswith(letter):
                name = current_name
                break

        result.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(result))




print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))