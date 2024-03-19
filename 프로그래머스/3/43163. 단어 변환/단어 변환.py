from collections import deque

def check_str(str_1, str_2):
    count = 0
    for char1, char2 in zip(str_1, str_2):
        if char1 != char2:
            count += 1
        if count >= 2:
            return False
    return True

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    words.append(begin)
    words_len = len(words)
    adj_list = [[] for _ in range(words_len)]
    for i, str_1 in enumerate(words):
        for j, str_2 in enumerate(words):
            if i >= j:
                continue
            if check_str(str_1, str_2):
                adj_list[i].append(j)
                adj_list[j].append(i)
    
    visit = [False] * words_len
    visit[words_len-1] = True
    distances = {words_len-1: 0}
    queue = deque([[words_len-1, 0]])
    
    while queue:
        node, distance = queue.popleft()
        neighbors = adj_list[node]
        for n in neighbors:
            if not visit[n]:
                visit[n] = True
                queue.append([n, distance+1])
                distances[n] = distance+1
        
    return distances[words.index(target)]