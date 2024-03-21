def solution(n, s):
    if n > s:
        return [-1]
    if not s % n:
        return [s // n] * n
    
    answer = []
    init_num = s // n
    answer.append(init_num)
    s -= init_num
    n -= 1
    while s % n:
        s -= init_num
        n -= 1        
        answer.append(init_num)
    
    for _ in range(n):
        answer.append(s // n)
        
    return answer