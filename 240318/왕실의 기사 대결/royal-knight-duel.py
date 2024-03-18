import sys
input = sys.stdin.readline

# Initialize
l, n, q = map(int, input().split())
move = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
board = [list(map(int, input().split())) for _ in range(l)]
knights = {i+1: list(map(int, input().split())) for i in range(n)}

knights_board = [[0 for _ in range(l)] for _ in range(l)]
for k in knights.keys():
    knights[k].append(knights[k][-1])
    knights[k][0] -= 1
    knights[k][1] -= 1
    r, c, h, w = knights[k][:4]
    for i in range(r, r+h):
        for j in range(c, c+w):
            knights_board[i][j] = k

def after_move(i):
    global knights, knights_board
    
    r, c, h, w, health = knights[i][:5]
    damage = 0

    for hr in range(h):
        for wc in range(w):
            new_r, new_c = r + hr, c + wc
            if board[new_r][new_c] == 1:
                damage += 1

    if damage > 0:
        knights[i][4] -= damage

    if knights[i][4] <= 0:
        del knights[i]
        for hr in range(h):
            for wc in range(w):
                new_r, new_c = r + hr, c + wc
                if 0 <= new_r < l and 0 <= new_c < l:
                    knights_board[new_r][new_c] = 0
    
def can_move(i, d):
    r, c, h, w = knights[i][:4]
    dr, dc = move[d]
    new_positions = [(r + dr + hr, c + dc + wc) for hr in range(h) for wc in range(w)]

    for new_r, new_c in new_positions:
        if new_r < 0 or new_r >= l or new_c < 0 or new_c >= l:
            return False
        if board[new_r][new_c] == 2:
            return False
        if knights_board[new_r][new_c] and knights_board[new_r][new_c] != i and not can_move(knights_board[new_r][new_c], d):
            return False
    return True

def move_knight(i, d):
    global knights_board, knights
    if i not in knights:
        return

    curr_knights = knights[i]
    r, c, h, w = curr_knights[:4]
    dr, dc = move[d]

    for hr in range(h):
        for wc in range(w):
            knights_board[r + hr][c + wc] = 0

    curr_knights[0] += dr
    curr_knights[1] += dc
    new_positions = [(r + dr + hr, c + dc + wc) for hr in range(h) for wc in range(w)]
    for new_r, new_c in new_positions:
        # Meet other knight
        tmp = knights_board[new_r][new_c]
        if tmp and tmp != i:
            move_knight(tmp, d)
            after_move(tmp)

        knights_board[new_r][new_c] = i

for _ in range(q):
    i, d = map(int, input().split())
    if knights.get(i, None) is not None:
        if can_move(i, d):
            move_knight(i, d)
    
    # for b in board:
    #     for bo in b:
    #         print(bo, end = ' ')
    #     print()
    # print("--------------------------------")
    # for k in knights_board:
    #     for kn in k:
    #         print(kn, end = ' ')
    #     print()

    # print(knights)

answer = 0
for info in knights.values():
    answer += (info[-1] - info[-2])
print(answer)