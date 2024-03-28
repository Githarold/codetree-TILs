n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))

ans = {}
for n in n_arr:
    ans[n] = ans.get(n, 0) + 1

for m in m_arr:
    print(ans.get(m, 0), end = ' ')