n, k = map(int, input().split())
answer = []

def print_answer():
    for a in answer:
        print(a, end = ' ')
    print()

def choose(curr_num):
    if curr_num == k+1:
        print_answer()
        return

    for i in range(1, n+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)