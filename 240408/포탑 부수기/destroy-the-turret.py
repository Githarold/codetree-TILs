from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 우, 하, 좌, 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 8방향
ddy = [-1, -1, -1, 0, 0, 1, 1, 1]
ddx = [1, 0, -1, 1, -1, 1, 0, -1]

attack = [[False] * m for _ in range(n)]
attack_info = [[0] * m for _ in range(n)]

def find_min():
    miny, minx = -1, -1
    min_power = float('inf')

    for i in range(n):
        for j in range(m):
            update = False
            if board[i][j] and board[i][j] < min_power:
                update = True
            elif board[i][j] == min_power:
                if attack_info[i][j] > attack_info[miny][minx]:
                    update = True
                elif attack_info[i][j] == attack_info[miny][minx]:
                    if i + j > miny + minx:
                        update = True
                    elif i + j == miny + minx:
                        if j > minx:
                            update = True
            if update:
                min_power = board[i][j]
                miny, minx = i, j

    return miny, minx

def find_max():
    maxy, maxx = -1, -1
    max_power = -1

    for i in range(n):
        for j in range(m):
            update = False
            if board[i][j] > max_power:
                update = True
            elif board[i][j] == max_power:
                if attack_info[i][j] < attack_info[maxy][maxx]:
                    update = True
                elif attack_info[i][j] == attack_info[maxy][maxx]:
                    if i + j < maxy + maxx:
                        update = True
                    elif i + j == maxy + maxx:
                        if j < maxx:
                            update = True
            if update:
                max_power = board[i][j]
                maxy, maxx = i, j

    return maxy, maxx

def attack_laser(si, sj, ei, ej):
    global board, attack
    damage = board[si][sj]
    attack[si][sj] = True
    attack[ei][ej] = True    

    flow = []
    def bfs(si, sj):
        q = deque([(si, sj, [])])
        visit = [[False] * m for _ in range(n)]
        visit[si][sj] = True

        while q:
            ci, cj, path = q.popleft()
            if [ci, cj] == [ei, ej]:
                flow.append(path + [[ci, cj]])
                continue

            for i in range(4):
                ni, nj = (ci + dy[i]) % n, (cj + dx[i]) % m
                if not visit[ni][nj] and board[ni][nj]:
                    visit[ni][nj] = True
                    q.append((ni, nj, path + [[ci, cj]]))

    bfs(si, sj)
    
    if flow:
        flow.sort(key=len)
        select_flow = flow[0]
        for y, x in select_flow:
            attack[y][x] = True
            board[y][x] -= damage // 2
        
        board[si][sj] += damage // 2
        board[ei][ej] += damage // 2
    else:
        for i in range(8):
            ni, nj = (ei + ddy[i]) % n, (ej + ddx[i]) % m
            if board[ni][nj] and [ni, nj] != [si, sj]:
                attack[ni][nj] = True
                board[ni][nj] -= damage // 2
    
    board[ei][ej] -= damage

def turn_over():
    global board, attack

    for i in range(n):
        for j in range(m):
            if board[i][j] < 0:
                board[i][j] = 0

            if attack[i][j]:
                attack[i][j] = False
                continue

            if board[i][j]:
                board[i][j] += 1    

for i in range(k):
    
    miny, minx = find_min()
    maxy, maxx = find_max()

    board[miny][minx] += (m + n)
    attack_info[miny][minx] = i+1

    attack_laser(miny, minx, maxy, maxx)

    count = 0
    for bo in board:
        for b in bo:
            if b > 0:
                count += 1

    if count == 1:
        break

    turn_over()

print(max(max(row) for row in board))