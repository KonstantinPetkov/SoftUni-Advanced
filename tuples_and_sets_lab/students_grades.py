number = int(input())
student_data = {}

for n in range(number):
    name, grades = input().split()
    if name not in student_data:
        student_data[name] = []
    student_data[name].append(float(grades))

for student_name, student_grade in student_data.items():
    avarage_grade = sum(student_grade) / len(student_grade)
    print(f"{student_name} -> {' '.join(map(lambda grade: f'{grade:.2f}', student_grade))} (avg: {avarage_grade:.2f})")

