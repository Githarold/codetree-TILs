import sys
from collections import deque
input = sys.stdin.readline

q = int(input().strip()) - 1
tmp = list(map(int, input().split()))
n, m = tmp[1:3]
belt_info = {i: True for i in range(m)}

belts = [deque() for _ in range(m)]
for i in range(n):
    belt_num = i // (n//m)
    belts[belt_num].append((tmp[i+3], tmp[i+n+3]))

def work1(w_max):
    global belts
    weight_sum = 0
    for i, belt in enumerate(belts):
        if belt_info[i] and belt:
            if belt[0][1] <= w_max:
                weight_sum += belt[0][1]
                belt.popleft()
            else:
                belt.append(belt.popleft())
    print(weight_sum)

def work2(r_id):
    global belts
    for i, belt in enumerate(belts):
        if belt_info[i] and belt:
            for b in list(belt):
                if b[0] == r_id:
                    belt.remove(b)
                    print(r_id)
                    return
    print(-1)

def work3(f_id):
    global belts
    for i, belt in enumerate(belts):
        if belt_info[i] and belt:
            belt_list = list(belt)
            belt_len = len(belt_list)
            for j, b in enumerate(belt_list):
                if b[0] == f_id:
                    for _ in range(j, belt_len):
                        belt.appendleft(belt.pop())
                    print(i+1)
                    return
    print(-1)

def work4(b_num):
    global belts, belt_info
    remove_belt = b_num-1
    add_belt = (remove_belt + 1) % m
    if belt_info[remove_belt]:
        belt_info[remove_belt] = False
        while belts[remove_belt]:
            belts[add_belt].append(belts[remove_belt].popleft())
        print(b_num)
    else:
        print(-1)

for _ in range(q):
    work, value = map(int, input().split())
    if work == 200:
        work1(value)
    elif work == 300:
        work2(value)
    elif work == 400:
        work3(value)
    else:
        work4(value)