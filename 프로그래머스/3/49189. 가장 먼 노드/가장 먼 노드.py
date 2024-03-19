from collections import deque

def solution(n, edge):
    adj_list = [[] for _ in range(n+1)]
    for s, e in edge:
        adj_list[s].append(e)
        adj_list[e].append(s)
        
    visit = [False] * (n + 1)
    visit[1] = True
    queue = deque([[1, 0]])
    distances = {1: 0}
    
    while queue:
        node, distance = queue.popleft()
        neighbors = adj_list[node]
        for n in neighbors:
            if not visit[n]:
                visit[n] = True
                distances[n] = distance + 1
                queue.append([n, distance + 1])
            
    sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=True)
    max_distance = sorted_distances[0][1]
    answer = 0
    for d in sorted_distances:
        if d[1] == max_distance:
            answer += 1
        else:
            return answer