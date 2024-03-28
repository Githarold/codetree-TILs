n, m = map(int, input().split())

str2num = {}
num2str = {}
for i in range(1, n+1):
    string = input()
    str2num[string] = i
    num2str[i] = string

for _ in range(m):
    tmp = input()
    if tmp.isdigit():
        print(num2str[int(tmp)])
    else:
        print(str2num[tmp])