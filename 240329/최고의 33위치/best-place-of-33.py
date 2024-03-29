n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
for y in range(n-2):
    for x in range(n-2):
        tmp = 0
        for dy in range(3):
            for dx in range(3):
                tmp += board[y+dy][x+dx]
        
        if tmp > answer:
            answer = tmp

print(answer)