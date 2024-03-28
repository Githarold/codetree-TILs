n = int(input())
students = []

for i in range(n):
    h, w = map(int, input().split())
    students.append((h, w, i + 1))

students.sort(key=lambda x: (x[0], -x[1], x[2]))

for student in students:
    print(student[0], student[1], student[2])