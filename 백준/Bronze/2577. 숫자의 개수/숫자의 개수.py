a = int(input())
b = int(input())
c = int(input())

result = a*b*c
r = str(result)

for i in range(10):
    count = 0
    for j in r:
        if i == int(j):
            count += 1
    print(count)