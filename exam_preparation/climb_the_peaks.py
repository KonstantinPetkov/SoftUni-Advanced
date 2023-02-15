from collections import deque

food_portions = list(map(int, input().split(", ")))
stamina = list(map(int, input().split(", ")))

food_deque = deque(food_portions)
stamina_deque = deque(stamina)

mountain_peak_level = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
conquered_peaks = []
failed = False

for key, value in mountain_peak_level.items():

    while True:
        daily_sum_of_elements = food_deque.pop() + stamina_deque.popleft()

        if daily_sum_of_elements >= value:
            conquered_peaks.append(key)
            break
        elif len(food_deque) == 0 or len(stamina_deque) == 0:
            failed = True
            break

    if failed:
        if len(conquered_peaks) == 0:
            print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
            break
        else:
            print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
            break

if not failed:
    data = '\n'.join(conquered_peaks)
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{data}")