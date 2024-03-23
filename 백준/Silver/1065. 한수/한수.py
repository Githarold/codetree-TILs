def plusnum(n):
    if 0 < n < 100:
        return 1
    else:
        num = list(str(n))
        if((int(num[0])-int(num[1]))==(int(num[1])-int(num[2]))):
            return 1
        else:
            return 0

total = 0
n = int(input())
for i in range(1,n+1):
    total += plusnum(i)

print(total)
