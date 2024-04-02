import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

answer = 0
for y in range(n):
    for x in range(m):
        tmp = []
        for dy, dx in move:
            new_y, new_x = [y+dy, x+dx]
            if new_y < 0 or new_y >= n or new_x < 0 or new_x >= m:
                continue
            
            tmp.append(board[new_y][new_x])
        
        tmp.sort()
        answer = max(answer, board[y][x] + tmp[-1] + tmp[-2])

print(answer)