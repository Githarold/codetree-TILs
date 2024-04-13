m, t = map(int, input().split())
pi, pj = list(x-1 for x in map(int, input().split()))
monster = [list(x-1 for x in map(int, input().split())) for _ in range(m)]
egg = set()
dead = set()

# 북, 북서, 서, 남서, 남, 남동, 동, 북동
# 상, 좌, 하, 우: 0, 2, 4, 6
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

def move_packman():
    global pi, pj, monster, dead

    tmp = []
    for i in [0, 2, 4, 6]:
        for j in [0, 2, 4, 6]:
            for k in [0, 2, 4, 6]:
                tmp.append((i, j, k))
    
    kill_tmp = []
    for route in tmp:
        ci, cj = pi, pj
        kill = 0
        kill_idx = set()
        for dr in route:
            ni, nj = ci + di[dr], cj + dj[dr]
            if not (0 <= ni < 4 and 0 <= nj < 4):
                kill = -1
                break

            for idx, (mi, mj, _) in enumerate(monster):
                if idx not in kill_idx and [ni, nj] == [mi, mj]:
                    kill_idx.add(idx)
                    kill += 1

            ci, cj = ni, nj

        kill_tmp.append((route, kill))

    kill_tmp.sort(key = lambda x: x[1], reverse = True)
    real_route = kill_tmp[0][0]

    for dr in real_route:
        ni, nj = pi + di[dr], pj + dj[dr]

        dead_idx = set()
        for idx, (mi, mj, _) in enumerate(monster):
            if [ni, nj] == [mi, mj]:
                dead_idx.add(idx)
                dead.add((ni, nj, 2))

        monster = [monster[i] for i in range(len(monster)) if i not in dead_idx]
        pi, pj = ni, nj

for _ in range(t):
    # 1, 2
    for idx, (mi, mj, dr) in enumerate(monster):
        egg.add((mi, mj, dr))

        ni, nj = mi + di[dr], mj + dj[dr]
        count = 1
        dead_set = set((d[0], d[1]) for d in dead)
        while not (0 <= ni < 4 and 0 <= nj < 4) or (ni, nj) in dead_set or [ni, nj] == [pi, pj]:
            dr = (dr + 1) % 8
            ni, nj = mi + di[dr], mj + dj[dr]
            count += 1
            if count > 8:
                ni, nj = mi, mj
                break
        monster[idx] = [ni, nj, dr]

    # 3
    move_packman()

    # 4
    updated_dead = set()
    for i, j, days in dead:
        if days == 0:
            continue
        updated_dead.add((i, j, days-1))
    dead = updated_dead

    for mi, mj, dr in egg:
        monster.append([mi, mj, dr])
    egg = set()

print(len(monster))