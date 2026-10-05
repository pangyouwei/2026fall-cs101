import sys


def main():
    data = sys.stdin.read().splitlines()
    # if not data:
    #     return
    n = int(data[0])
    header = data[1].split()
    idx = {col: i for i, col in enumerate(header)}
    students = []
    for i in range(n):
        parts = data[2 + i].split()
        name = parts[idx['Name']]
        gender = parts[idx['Gender']]
        chinese = int(parts[idx['Chinese']])
        math = int(parts[idx['Math']])
        english = int(parts[idx['English']])
        birth = parts[idx['Birth']]
        height = float(parts[idx['Height']])
        total = chinese + math + english
        students.append({
            'name': name,
            'gender': gender,
            'chinese': chinese,
            'math': math,
            'english': english,
            'birth': birth,
            'height': height,
            'total': total
        })

    sorted_students = sorted(students, key=lambda x: x['total'], reverse=True)
    print(sorted_students[0]['name'], sorted_students[0]['total'])

    quarters = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
    for student in students:
        month = int(student['birth'].split('-')[1])
        if 1 <= month <= 3:
            quarters['Q1'].append(student)
        elif 4 <= month <= 6:
            quarters['Q2'].append(student)
        elif 7 <= month <= 9:
            quarters['Q3'].append(student)
        else:
            quarters['Q4'].append(student)
    for quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
        count = len(quarters[quarter])
        average_height = sum(student['height'] for student in quarters[quarter]) / count if count else 0.0
        print(f"{quarter} {count} {average_height:.1f}")

    excellent_girls = []
    for student in students:
        if student['gender'] == 'F':
            average_score = student['total'] / 3
            if average_score >= 80 and student['chinese'] >= 70 and student['math'] >= 70 and student['english'] >= 70:
                excellent_girls.append(student)
    print(len(excellent_girls))
    excellent_girls.sort(key=lambda x: (-x['total'], x['name']))
    for student in excellent_girls:
        print(f"{student['name']} {student['chinese']} {student['math']} {student['english']} {student['total']}")


if __name__ == '__main__':
    main()
