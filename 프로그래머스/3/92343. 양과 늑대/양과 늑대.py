def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for a, b in edges:
        graph[a].append(b)
    
    answer = 0
    
    def dfs(sheep, wolf, current, next_nodes):
        nonlocal answer
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1
        
        answer = max(answer, sheep)
        
        if wolf >= sheep:
            return
        
        for next_node in next_nodes:
            dfs(sheep, wolf, next_node, next_nodes - {next_node} | set(graph[next_node]))
    
    dfs(0, 0, 0, set(graph[0]))
    
    return answer