import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
for i in range(n):
    for j in range(i+1, n):
        sum = arr[i] + arr[j]
        dic[sum] = dic.get(sum, 0) + 1

print(dic[k])