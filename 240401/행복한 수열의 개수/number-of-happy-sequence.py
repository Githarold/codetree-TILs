import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    last_num1 = None
    last_num2 = None
    cnt1 = 1
    cnt2 = 1
    for j in range(n):
        if last_num1 and board[i][j] == last_num1:
            cnt1 += 1
        else:
            cnt1 = 1
            last_num1 = board[i][j]

        if cnt1 >= m:
            answer += 1
            cnt1 = -100

        if last_num2 and board[j][i] == last_num2:
            cnt2 += 1
        else:
            cnt2 = 1
            last_num2 = board[j][i]

        if cnt2 >= m:
            answer += 1
            cnt2 = -100

print(answer)