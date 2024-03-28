n = int(input())

ans = {}
for _ in range(n):
    ins = list(input().split())
    if ins[0] == 'add':
        k, v = ins[1:]
        ans[k] = v
    elif ins[0] == 'remove':
        k = ins[1]
        ans.pop(k)
    else:
        k = ins[1]
        if k in ans:
            print(ans[k])
        else:
            print("None")