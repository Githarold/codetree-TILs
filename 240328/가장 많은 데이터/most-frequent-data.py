n = int(input())

ans = {}
answer = 0
for _ in range(n):
    tmp = input()
    ans[tmp] = ans.get(tmp, 0) + 1
    answer = max(answer, ans[tmp])

print(answer)