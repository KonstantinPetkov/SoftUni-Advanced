from collections import deque

textiles = list(map(int, input().split()))
medicaments = list(map(int, input().split()))

textiles_deque = deque(textiles)
medicaments_deque = deque(medicaments)

items_dict = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}
matched_dict = {}

while textiles_deque and medicaments_deque:

    textile_value = textiles_deque.popleft()
    medicament_value = medicaments_deque.pop()
    total_sum = textile_value + medicament_value

    if total_sum == 30:
        if 'Patch' not in matched_dict:
            matched_dict['Patch'] = 0
        matched_dict['Patch'] += 1

    elif total_sum == 40:
        if 'Bandage' not in matched_dict:
            matched_dict['Bandage'] = 0
        matched_dict['Bandage'] += 1

    elif total_sum == 100:
        if 'MedKit' not in matched_dict:
            matched_dict['MedKit'] = 0
        matched_dict['MedKit'] += 1

    elif total_sum > 100:

        if 'MedKit' not in matched_dict:
            matched_dict['MedKit'] = 0
        matched_dict['MedKit'] += 1

        remaining_sum = total_sum - 100
        medicaments_deque.append(remaining_sum)

    if total_sum != 30 and total_sum != 40 and total_sum != 100 and total_sum < 100:
        medicament_value += 10
        medicaments_deque.append(medicament_value)

    if not textiles_deque or not medicaments_deque:
        break





if not textiles_deque:
    print("Textiles are empty.")
if not medicaments_deque:
    print("Medicaments are empty.")
if not textiles_deque and not medicaments_deque:
    print("Textiles and medicaments are both empty.")

if matched_dict:
    sorted_data = sorted(matched_dict.items(), key=lambda x: (-x[1], x))
    for key, value in sorted_data:
        print(f"{key} - {value}")

if medicaments_deque:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments_deque])}")
if textiles_deque:
    print(f"Textiles left: {', '.join([str(x) for x in textiles_deque])}")