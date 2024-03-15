n = int(input())

def beautiful_num(n):
    if not n:
        return 1

    numbers = [1, 2, 3, 4]
    count = 0
    for num in numbers:
        if n >= num:
            count += beautiful_num(n - num)

    return count

print(beautiful_num(n))