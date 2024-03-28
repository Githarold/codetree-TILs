import sys
input = sys.stdin.readline

n = int(input().strip())

dic = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x in dic:
        if y < dic[x]:
            dic[x] = y
    else:
        dic[x] = y
    
answer = 0
for key in list(dic.keys()):
    answer += dic[key]

print(answer)