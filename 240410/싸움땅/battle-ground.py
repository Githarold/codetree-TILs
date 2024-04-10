import heapq

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        board[i][j].append(-tmp[j])

point = [0] * m
player = []
for _ in range(m):
    i, j, d, s = map(int, input().split())
    player.append([i-1, j-1, d, s, 0])

# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def win_player(idx, score):
    global point, player, board
    i, j, d, s, g = player[idx]
    point[idx] += score

    # Change gun
    if board[i][j]:
        ng = -heapq.heappop(board[i][j])
        heapq.heappush(board[i][j], -min(ng, g))
        player[idx][4] = max(ng, g)

def lose_player(idx):
    global player, board
    i, j, d, s, g = player[idx]
    player[idx][4] = 0
    heapq.heappush(board[i][j], g)
    for x in range(4):
        ni, nj = i + di[(d+x) % 4], j + dj[(d+x) % 4]

        if not (0 <= ni < n and 0 <= nj < n):
            continue

        player_flag = False
        for p in range(m):
            if p == idx:
                continue
            ti, tj, _, _, _ = player[p]
            if [ni, nj] == [ti, tj]:
                player_flag = True
                break

        if player_flag:
            continue
        else:
            break

    player[idx][2] = (d+x) % 4
    player[idx][0], player[idx][1] = ni, nj

    if board[ni][nj]:
        player[idx][4] = -heapq.heappop(board[ni][nj])

def fight(p1, p2):
    _, _, _, s1, g1 = player[p1]
    _, _, _, s2, g2 = player[p2]
    score = abs(s1 + g1 - s2 - g2)

    if s1 + g1 > s2 + g2:
        lose_player(p2), win_player(p1, score)
    elif s1 + g1 < s2 + g2:
        lose_player(p1), win_player(p2, score)
    else:
        if s1 > s2:
            lose_player(p2), win_player(p1, score)
        else:
            lose_player(p1), win_player(p2, score)

for _ in range(k):
    for p in range(m):

        # Move the player
        i, j, d, s, g = player[p]
        ni, nj = i + di[d], j + dj[d]
        if not (0 <= ni < n and 0 <= nj < n):
            player[p][2] = (d + 2) % 4
            ni, nj = i - di[d], j - dj[d]
        player[p][0], player[p][1] = ni, nj

        player_flag = False
        for op in range(m):
            if op == p:
                continue
            i, j, _, _, _ = player[op]
            if [i, j] == [ni, nj]:
                player_flag = True
                break

        # Fight
        if player_flag:
            fight(p, op)
        else:
            if board[ni][nj]:
                ng = -heapq.heappop(board[ni][nj])
                heapq.heappush(board[ni][nj], -min(ng, g))
                player[p][4] = max(ng, g)
        
    # for b in board:
    #     print(b)
    # print(player)

print(*point)