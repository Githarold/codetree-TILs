from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
goal = [list(x-1 for x in map(int, input().split())) for _ in range(m)]
base = [[i, j] for i in range(n) for j in range(n) if board[i][j]]
player = [[-1, -1] for _ in range(m)]
is_goal = [False] * m

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def find_path(si, sj, ei, ej):
    q = deque([(si, sj, [])])
    visit = [[False] * n for _ in range(n)]
    visit[si][sj] = True
    route = []

    while q:
        ci, cj, path = q.popleft()
        if [ci, cj] == [ei, ej]:
            route.append(path + [[ci, cj]])
        
        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]
            if 0 <= ni < n and 0 <= nj < n and not visit[ni][nj] and board[ni][nj] != -1:
                visit[ni][nj] = True
                q.append((ni, nj, path + [[ci, cj]]))

    if not route:
        return float('inf')
    else:
        route.sort()
        return len(route[0])

def find_base(idx):
    mi, mj = -1, -1
    gi, gj = goal[idx]
    min_dist = float('inf')

    for bi, bj in base:
        dist = find_path(bi, bj, gi, gj)
        if dist < min_dist:
            min_dist = dist
            mi, mj = bi, bj
        elif dist == min_dist:
            if bi < mi:
                min_dist = dist
                mi, mj = bi, bj
            elif bi == mi:
                if bj < mj:
                    min_dist = dist
                    mi, mj = bi, bj
    return mi, mj

def go_ahead():
    global player

    for i in range(m):
        if not is_goal[i] and player[i] != [-1, -1]:
            min_dist = float('inf')
            mi, mj = -1, -1
            for j in range(4):
                ni, nj = player[i][0] + di[j], player[i][1] + dj[j]
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != -1:
                    # new_dist = abs(ni - goal[i][0]) + abs(nj - goal[i][1])
                    new_dist = find_path(ni, nj, goal[i][0], goal[i][1])
                    if new_dist < min_dist:
                        min_dist = new_dist
                        mi, mj = ni, nj

            player[i] = [mi, mj]

counter = 0
while True:
    go_ahead()

    if counter < m:
        bi, bj = find_base(counter)
        base.remove([bi, bj])
        player[counter] = [bi, bj]    
        board[bi][bj] = -1

    for i in range(m):
        if not is_goal[i] and player[i] == goal[i]:
            is_goal[i] = True
            board[goal[i][0]][goal[i][1]] = -1

    counter += 1
    if is_goal.count(True) == m:
        break

print(counter)