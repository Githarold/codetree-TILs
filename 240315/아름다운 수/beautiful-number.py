n = int(input())

def beautiful_num(n):
    if not n:
        return 1

    count = 0
    for num in range(1, 5):
        if n >= num:
            count += beautiful_num(n - num)

    return count

print(beautiful_num(n))