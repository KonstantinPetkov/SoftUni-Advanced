def students_credits(*data):
    courses = {}
    output = []

    for current_data in data:
        splitted_data = current_data.split('-')
        course_name = splitted_data[0]
        credits = int(splitted_data[1])
        max_points = int(splitted_data[2])
        points = int(splitted_data[3])
        courses[course_name] = credits * (points / max_points)

    total_credits = sum(courses.values())

    if total_credits >= 240:
        output.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        output.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    sorted_data = sorted(courses.items(), key=lambda v: -(v[1]))
    for key, value in sorted_data:
        output.append(f'{key} - {value:.1f}')

    return '\n'.join(output)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

