def solution(n, computers):
    answer = 0
    def dfs(x):
        for idx, j in enumerate(computers[x]):
            computers[x][idx] = computers[idx][x] = 0
            if j and 1 in computers[idx]:
                dfs(idx)

    for i in range(n):
        if 1 in computers[i]:
            dfs(i)
            answer += 1
    return answer