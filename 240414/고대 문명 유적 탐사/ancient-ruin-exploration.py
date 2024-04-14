from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
m_list = deque(list(map(int, input().split())))

def bfs(bfs_board):
    cur_visit = set()
    cur_list = []
    cur_value = 0
    for i in range(5):
        for j in range(5):
            if (i, j) not in cur_visit:
                val = 1  # 처음 발견된 타일도 카운트에 포함
                tmp_visit = set([(i, j)])
                tmp_list = [(i, j)]
                q = deque([(i, j)])

                while q:
                    ci, cj = q.popleft()
                    for dr in range(4):
                        ni, nj = ci + di[dr], cj + dj[dr]
                        if 0 <= ni < 5 and 0 <= nj < 5 and (ni, nj) not in tmp_visit and bfs_board[ni][nj] == bfs_board[ci][cj]:
                            q.append((ni, nj))
                            tmp_visit.add((ni, nj))
                            tmp_list.append((ni, nj))
                            val += 1

                if val >= 3:  # 연결된 조각이 3개 이상일 경우에만 유물로 간주
                    cur_value += val
                    cur_list.extend(tmp_list)
                    cur_visit.update(tmp_list)  # 처리된 타일들을 방문 처리

    return cur_value, cur_list


def find_rotate():
    row, cul, rotate = -1, -1, -1
    max_value = 2
    for c in range(3):
        for r in range(3):
            for rot in range(3):
                tmp_board = [[0]*5 for _ in range(5)]
                tmp = [[0]*3 for _ in range(3)]
                for i in range(5):
                    for j in range(5):
                        tmp_board[i][j] = board[i][j]

                for i in range(3):
                    for j in range(3):
                        if rot == 0:
                            tmp[j][2-i] = board[r+i][c+j]
                        elif rot == 1:
                            tmp[2-i][2-j] = board[r+i][c+j]
                        elif rot == 2:
                            tmp[2-j][i] = board[r+i][c+j]

                for i in range(3):
                    for j in range(3):
                        tmp_board[r+i][c+j] = tmp[i][j]
                
                value, _ = bfs(tmp_board)

                if value > max_value:
                    max_value = value
                    row, cul, rotate = r, c, rot
                elif value == max_value:
                    if rot < rotate:
                        max_value = value
                        row, cul, rotate = r, c, rot
    
    return row, cul, rotate


def rotate_box(r, c, rot):
    global board
    temp = [[board[r+i][c+j] for j in range(3)] for i in range(3)]
    if rot == 0:  # 90 degrees
        for i in range(3):
            for j in range(3):
                board[r+j][c+2-i] = temp[i][j]
    elif rot == 1:  # 180 degrees
        for i in range(3):
            for j in range(3):
                board[r+2-i][c+2-j] = temp[i][j]
    elif rot == 2:  # 270 degrees
        for i in range(3):
            for j in range(3):
                board[r+2-j][c+i] = temp[i][j]
    

for _ in range(k):
    answer = 0
    r, c, rot = find_rotate()
    if rot == -1:
        break
    rotate_box(r, c, rot)
    max_value, score_list = bfs(board)
    answer += max_value

    score_list.sort(key = lambda x: (x[1], -x[0]))
    for si, sj in score_list:
        board[si][sj] = m_list.popleft()

    max_value, score_list = bfs(board)
    while max_value > 0:
        answer += max_value
        score_list.sort(key = lambda x: (x[1], -x[0]))
        for si, sj in score_list:
            board[si][sj] = m_list.popleft()
        
        max_value, score_list = bfs(board)

    print(answer, end=' ')