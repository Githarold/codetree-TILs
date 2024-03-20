from heapq import heapify, heappop, heappush

def solution(n, works):
    works = [-work for work in works]
    heapify(works)
    
    for _ in range(n):
        if not works[0]:
            break
        heappush(works, heappop(works) + 1)
        
    return sum(work ** 2 for work in works)
