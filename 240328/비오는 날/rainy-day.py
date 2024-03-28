import sys
input = sys.stdin.readline

def early(day1, day2):
    date1, _ = day1.split()
    date2, _ = day2.split()
    y1, m1, d1 = map(int, date1.split('-'))
    y2, m2, d2 = map(int, date2.split('-'))

    flag = True
    if y1 < y2:
        flag = False
    elif y1 == y2:
        if m1 < m2:
            flag = False
        elif m1 == m2:
            if d1 < d2:
                flag = False

    if flag:
        return day2
    else:
        return day1

rainy = None
n = int(input().strip())
for _ in range(n):
    date, weekday, wether = input().split()
    if wether == "Rain":
        tmp_day = date + ' ' + weekday
        if not rainy:
            rainy = tmp_day
        else:
            rainy = early(tmp_day, rainy)

print(rainy, 'Rain')