n, m, h, k = map(int, input().split())
runner = [list(map(int, input().split())) for _ in range(m)]
tree = [tuple(map(int, input().split())) for _ in range(h)]
out = [False] * m

# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

max_cnt, cnt, flag, val = 1, 0, 0, 1
s = (n + 1) // 2
ti, tj, d = s, s, 0

def move_runner():
    global runner
    for idx, (i, j, d) in enumerate(runner):
        if out[idx]:
            continue

        if abs(ti - i) + abs(tj - j) <= 3:
            ni, nj = i + di[d], j + dj[d]
            if [ni, nj] == [ti, tj]:
                continue
            if not (0 < ni <= n and 0 < nj <= n):
                ni, nj = i - di[d], j - dj[d]
                d = (d + 2) % 4
            runner[idx] = [ni, nj, d]

def get_runner(k):
    global out
    get_count = 0
    tmp = [(ti, tj), (ti + di[d], tj + dj[d]), (ti + 2*di[d], tj + 2*dj[d])]
    for idx, (i, j, rd) in enumerate(runner):
        if out[idx]:
            continue
        if (i, j) in tmp and (i, j) not in tree:
            get_count += 1
            out[idx] = True
    
    return get_count * k

answer = 0
for step in range(1, k+1):
    move_runner()
    cnt += 1
    ti, tj = ti + di[d], tj + dj[d]
    if (ti, tj) == (1, 1):
        max_cnt, cnt, flag, val = n, 1, 1, -1
        d = 2
    elif (ti, tj) == (s, s):
        max_cnt, cnt, flag, val = 1, 0, 0, 1
        d = 0
    else:
        if cnt == max_cnt:
            cnt = 0
            d = (d + val) % 4
            if flag:
                flag = 0
                max_cnt += val
            else:
                flag = 1
                
    answer += get_runner(step)

print(answer)