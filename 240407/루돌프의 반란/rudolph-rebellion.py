n, m, p, c, d = map(int, input().split())
ry, rx = list(x-1 for x in map(int, input().split()))
santa = []
board = [[0] * n for _ in range(n)]
for _ in range(p):
    _, y, x = map(int, input().split())
    santa.append([y-1, x-1])
    board[y-1][x-1] = 1

stun = [False] * p
out = [0] * p
score = [0] * p

def find_santa():
    y, x = -1, -1
    mind = 2 * n
    for i, [sy, sx] in enumerate(santa):
        if out[i]:
            continue
        dist = (ry - sy) ** 2 + (rx - sx) ** 2
        if dist <= mind:
            if sy > y:
                mind = dist
                y, x = sy, sx
                index = i
            elif sy == y:
                if sx > x:
                    mind = dist
                    y, x = sy, sx
                    index = i

    return y, x, index

def push_santa(index, dy, dx):
    global board, santa, out
    dy, dx = -dy, -dx
    ny, nx = santa[index][0] + dy, santa[index][1] + dx  # 한 칸만 이동할 새 위치

    # 밀려난 위치가 보드 밖인 경우 산타 탈락
    if not (0 <= ny < n and 0 <= nx < n):
        board[santa[index][0]][santa[index][1]] = 0
        out[index] = True
        return

    # 밀려난 위치에 다른 산타가 있는 경우, 해당 산타도 한 칸 밀림
    for i, [sy, sx] in enumerate(santa):
        if [ny, nx] == [sy, sx] and not out[i]:
            push_santa(i, dy, dx)  # 다음 산타를 밀어냄
            break

    # 최종적으로 밀려난 위치로 산타 이동
    if not out[index]:  # 아직 탈락하지 않았다면 이동
        board[santa[index][0]][santa[index][1]] = 0
        santa[index] = [ny, nx]
        board[ny][nx] = 1

def hit(dy, dx, index, flag):
    global score, stun, board, santa, out
    scarla = d if flag else c
    score[index] += scarla
    stun[index] = 2

    # 밀려날 산타의 최종 위치 계산
    final_y, final_x = santa[index][0] - dy * scarla, santa[index][1] - dx * scarla

    # 최종 위치가 보드 밖인 경우 산타 탈락
    if not (0 <= final_y < n and 0 <= final_x < n):
        board[santa[index][0]][santa[index][1]] = 0
        out[index] = True
        return

    # 최종 위치로 바로 이동
    board[santa[index][0]][santa[index][1]] = 0
    if board[final_y][final_x] == 1:  # 최종 위치에 다른 산타가 있는 경우 한 칸 밀림
        for i, [sy, sx] in enumerate(santa):
            if [final_y, final_x] == [sy, sx] and not out[i]:
                push_santa(i, dy, dx)
                break
    if not out[index]:  # 탈락하지 않았다면 최종 위치 업데이트
        santa[index] = [final_y, final_x]
        board[final_y][final_x] = 1

def move_dolf():
    global ry, rx
    sy, sx, i = find_santa()
    dy, dx = sy - ry, sx - rx

    if dy < 0:
        ry -= 1
    elif dy > 0:
        ry += 1
    if dx < 0:
        rx -= 1
    elif dx > 0:
        rx += 1
    
    if [ry, rx] == [sy, sx]:
        hit(-dy, -dx, i, 0)

def move_santa():
    global santa, board
    for i, [sy, sx] in enumerate(santa):
        if out[i]:
            continue
        if stun[i]:
            stun[i] -= 1
            continue
        
        dy, dx = ry - sy, rx - sx
        if dy < 0 and not board[sy-1][sx]:
            santa[i][0] -= 1
            board[sy][sx] = 0
            board[sy-1][sx] = 1
        elif dx > 0 and not board[sy][sx+1]:
            santa[i][1] += 1
            board[sy][sx] = 0
            board[sy][sx+1] = 1
        elif dy > 0 and not board[sy+1][sx]:
            santa[i][0] += 1
            board[sy][sx] = 0
            board[sy+1][sx] = 1
        elif dx < 0 and not board[sy][sx-1]:
            santa[i][1] -= 1
            board[sy][sx] = 0
            board[sy][sx-1] = 1

        if [ry, rx] == santa[i]:
            hit(dy, dx, i, 1)

# Main function
for _ in range(m):
    # board[ry][rx] = 'R'
    # for b in board:
    #     print(b)
    # board[ry][rx] = 0
    # print("-----------------------------------")
    move_dolf()
    move_santa()
    # board[ry][rx] = 'R'
    # for b in board:
    #     print(b)
    # board[ry][rx] = 0
    if out.count(True) == p:
        break
    for i in range(p):
        if not out[i]:
            score[i] += 1

for s in score:
    print(s, end=' ')