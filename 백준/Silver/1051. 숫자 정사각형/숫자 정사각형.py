n, m = map(int, input().split())
rectangle = [input() for _ in range(n)]

def find_largest_square():
    max_side = 0
    
    for i in range(n):
        for j in range(m):
            for k in range(min(n, m)):
                if i + k < n and j + k < m:
                    if rectangle[i][j] == rectangle[i][j+k] == rectangle[i+k][j] == rectangle[i+k][j+k]:
                        max_side = max(max_side, k+1)
    
    return max_side ** 2

print(find_largest_square())
