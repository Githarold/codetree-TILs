import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
for row in board:
    for i in range(n-m+1):
        if row[i:i+m].count(row[i]) == m:
            answer += 1
            break

for cow in zip(*board):
    for i in range(n-m+1):
        if cow[i:i+m].count(cow[i]) == m:
            answer += 1
            break

print(answer)