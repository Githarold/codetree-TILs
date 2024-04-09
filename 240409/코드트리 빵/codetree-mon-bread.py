n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
goal = [list(x-1 for x in map(int, input().split())) for _ in range(m)]
base = [[i, j] for i in range(n) for j in range(n) if board[i][j]]
player = [[-1, -1] for _ in range(m)]
is_goal = [False] * m

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def find_base(idx):
    mi, mj = -1, -1
    gi, gj = goal[idx]
    min_dist = float('inf')

    for bi, bj in base:
        dist = abs(gi - bi) + abs(gj - bj)
        if dist < min_dist:
            min_dist = dist
            mi, mj = bi, bj
        elif dist == min_dist:
            if bi < mi:
                min_dist = dist
                mi, mj = bi, bj
            elif bi == mi:
                if bj < mj:
                    min_dist = dist
                    mi, mj = bi, bj
    return mi, mj

def go_ahead():
    global player

    for i in range(m):
        if not is_goal[i] and player[i] != [-1, -1]:
            min_dist = float('inf')
            mi, mj = -1, -1
            for j in range(4):
                ni, nj = player[i][0] + di[j], player[i][1] + dj[j]
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != -1:
                    new_dist = abs(ni - goal[i][0]) + abs(nj - goal[i][1])
                    if new_dist < min_dist:
                        min_dist = new_dist
                        mi, mj = ni, nj

            player[i] = [mi, mj]

counter = 0
while True:
    go_ahead()

    if counter < m:
        bi, bj = find_base(counter)
        base.remove([bi, bj])
        player[counter] = [bi, bj]    
        board[bi][bj] = -1
aN, M = map(int, input().split())
arr = [[1]*(N+2)]+[[1]+list(map(int,input().split()))+[1] for _ in range(N)]+[[1]*(N+2)]

basecamp = set()                    # basecamp
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j]==1:
            basecamp.add((i,j))
            arr[i][j]=0

store = {}                          # 편의점
for m in range(1,M+1):
    i,j = map(int, input().split())
    store[m]=(i,j)

from collections import deque
def find(si,sj,dests):  # 시작좌표에서 목적지좌표들(set)중 최단거리 동일반경 리스트를 모두 찾기!
    q = deque()
    v = [[0]*(N+2) for _ in range(N+2)]
    tlst = []

    q.append((si,sj))
    v[si][sj]=1

    while q:
        # 동일 범위(반경)까지 처리
        nq = deque()
        for ci,cj in q:
            if (ci,cj) in dests:    # 목적지 찾음! => 더 뻗어나갈 필요없음
                tlst.append((ci,cj))
            else:
                # 네방향, 미방문, 조건: 벽이 아니면 arr[][]==0
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=ci+di, cj+dj
                    if v[ni][nj]==0 and arr[ni][nj]==0:
                        nq.append((ni,nj))
                        v[ni][nj]=v[ci][cj]+1
        # 목적지 찾았다면(여러개 일수도..) 리턴
        if len(tlst)>0:
            tlst.sort()             # 행/열 오름차순
            return tlst[0]
        q = nq
    # 이곳에 올리는 없지만....
    return -1

def solve():
    q = deque()
    time = 1
    arrived = [0]*(M+1)     # 0이면 미도착, >0 이면 도착시간

    while q or time==1:    # 처음 또는 q에 데이터 있는동안(이동할 사람이 있는 동안) 실행
        nq = deque()
        alst = []
        # [1] 모두 편의점방향 최단거리 이동 (이번 time만, 같은 반경)
        for ci,cj,m in q:
            if arrived[m]==0:   # 도착하지 않은 사람만 처리
                # 편의점방향 최단거리(우선순위) 한 칸 이동
                # 편의점에서 시작, 현재위치(상/하/좌/우 => dests (set) )
                ni,nj=find(store[m][0],store[m][1],set(((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1))))
                if (ni,nj)==store[m]:       # 최종 편의점에 도착
                    arrived[m]=time
                    alst.append((ni,nj))    # 통행금지는 모두 이동후 처리해야 함!!
                else:
                    nq.append((ni,nj,m))    # 계속 이동
        q=nq

        # [2] 편의점 도착처리 => arr[][]=1 (이동불가처리)
        if len(alst)>0:
            for ai,aj in alst:
                arr[ai][aj]=1               # 이동불가

        # [3] 시간번호의 멤버가 베이스캠프로 순간이동
        if time<=M:
            si,sj=store[time]
            ei,ej=find(si,sj,basecamp)  # 가장 가까운(우선순위 높은) 베이스캠프 선택
            basecamp.remove((ei,ej))
            arr[ei][ej]=1               # 이동불가
            q.append((ei,ej,time))      # 베이스캠프에서 이동시작

        time+=1
    return max(arrived)

ans = solve()
print(ans)
    for i in range(m):
        if not is_goal[i] and player[i] == goal[i]:
            is_goal[i] = True
            board[goal[i][0]][goal[i][1]] = -1

    counter += 1
    if is_goal.count(True) == m:
        break

print(counter)