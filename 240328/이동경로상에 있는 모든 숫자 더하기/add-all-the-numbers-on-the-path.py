import sys
input = sys.stdin.readline

n, _ = map(int, input().split())
ins = list(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

direction = ['N', 'E', 'S', 'W']
move = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
dir_idx = 0
y, x = [n//2, n//2]
answer = board[y][x]
for i in ins:
    if i == "R":
        dir_idx = (dir_idx + 1) % 3
    elif i == "L":
        dir_idx -= 1
        if dir_idx < 0:
            dir_idx = 3
    elif i == "F":
        dy, dx = move[direction[dir_idx]]
        y += dy
        x += dx
        if y < 0 or y >= n or x < 0 or x >= n:
            y -= dy
            x -= dx
            continue
        answer += board[y][x]

print(answer)