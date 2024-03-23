max = 0
maxth = 0

for i in range(9):
    num = int(input())
    if num > max:
        max = num
        maxth = i+1

print(max)
print(maxth)