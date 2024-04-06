n, m, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

player = [list(x - 1 for x in map(int, input().split())) for _ in range(m)]
exit = list(x - 1 for x in map(int, input().split()))
dist = 0

# Player moving method
def move_player():
    global player, dist

    for i, (y, x) in enumerate(player):
        dy = exit[0] - y
        dx = exit[1] - x

        if dy < 0:
            if not board[y-1][x]:
                player[i][0] -= 1
                dist += 1
                continue
        elif dy > 0:
            if not board[y+1][x]:
                player[i][0] += 1
                dist += 1
                continue
        
        if dx < 0:
            if not board[y][x-1]:
                player[i][1] -= 1
                dist += 1
        elif dx > 0:
            if not board[y][x+1]:
                player[i][1] += 1
                dist += 1

    player = [p for p in player if p != exit]

# Find minimum size square
def find_square():
    ey, ex = exit

    for size in range(2, n+1):
        for y1 in range(n+1-size):
            for x1 in range(n+1-size):
                x2, y2 = [x1 + size - 1, y1 + size - 1]

                if not (y1 <= ey <= y2 and x1 <= ex <= x2):
                    continue
                
                for y, x in player:
                    if y1 <= y <= y2 and x1 <= x <= x2:
                        return y1, x1, size

# Rotate square method
def rotate_square(r, c, size):
    global board, exit, player

    tmp = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            tmp[j][size-1-i] = board[r+i][c+j]
    
    for i in range(size):
        for j in range(size):
            if tmp[i][j]:
                tmp[i][j] -= 1
            board[r+i][c+j] = tmp[i][j]
    
    if r <= exit[0] < r + size and c <= exit[1] < c + size:
        ey, ex = exit
        exit = [r + (ex - c), c + (size - 1 - (ey - r))]

    for i in range(len(player)):
        y, x = player[i]
        if r <= y < r + size and c <= x < c + size:
            player[i] = [r + (x - c), c + (size - 1 - (y - r))]
    
for _ in range(k):
    move_player()
    
    if not player:
        break

    r, c, size = find_square()
    rotate_square(r, c, size)

print(dist)
print(exit[0]+1, exit[1]+1)