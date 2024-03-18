import sys
from collections import deque
input = sys.stdin.readline

q = int(input().strip()) - 1
tmp = list(map(int, input().split()))
n, m = tmp[1:3]
belt_info = {i: True for i in range(m)}
box_info = {}

belts = [deque() for _ in range(m)]
for i in range(n):
    belt_num = i // (n//m)
    box_id, box_weight = tmp[i+3], tmp[i+n+3]
    belts[belt_num].append((box_id, box_weight))
    box_info[box_id] = belt_num

def work1(w_max):
    global belts, box_info
    weight_sum = 0
    for i, belt in enumerate(belts):
        if belt_info[i] and belt:
            if belt[0][1] <= w_max:
                weight_sum += belt[0][1]
                tmp = belt.popleft()
                del box_info[tmp[0]]
            else:
                belt.append(belt.popleft())

    print(weight_sum)

def work2(r_id):
    global belts, box_info
    belt_num = box_info.get(r_id, None)
    if belt_num is None:
        print(-1)
    else:
        curr_belt = belts[belt_num]
        if belt_info[belt_num] and curr_belt:
            for b in list(curr_belt):
                if b[0] == r_id:
                    curr_belt.remove(b)
                    del box_info[b[0]]
                    print(r_id)
                    return        

def work3(f_id):
    global belts
    belt_num = box_info.get(f_id, None)
    if belt_num is None:
        print(-1)
    else:
        print(belt_num + 1)
        curr_belt = belts[belt_num]
        if belt_info[belt_num] and curr_belt:
            belt_list = list(curr_belt)
            belt_len = len(belt_list)
            for j, b in enumerate(belt_list):
                if b[0] == f_id:
                    for _ in range(j, belt_len):
                        curr_belt.appendleft(curr_belt.pop())
                    return

def work4(b_num):
    global belts, belt_info, box_info
    remove_belt = b_num-1
    if belt_info[remove_belt]:
        belt_info[remove_belt] = False
        add_belt = remove_belt
        while not belt_info[add_belt]:
            add_belt = (add_belt + 1) % m
        while belts[remove_belt]:
            append_item = belts[remove_belt].popleft()
            box_info[append_item[0]] = add_belt
            belts[add_belt].append(append_item)
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