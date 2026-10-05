# http://cs101.openjudge.cn/pctbook/E07618/

n = int(input())
old_patients = []
young_patients = []

for i in range(n):
    patient_id, age_str = input().split()
    age = int(age_str)

    if age >= 60:
        old_patients.append([patient_id, age])
    else:
        young_patients.append(patient_id)

old_patients.sort(key=lambda x: x[1], reverse=True)

for p in old_patients:
    print(p[0])
for p in young_patients:
    print(p)
