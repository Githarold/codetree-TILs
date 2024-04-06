n, m = map(int, input().split())
cost = [k*k + (k+1)*(k+1) for k in range(n//2+1)]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def max_gold_mining(n, m, grid):
    def count_gold_and_cost(k):
        cost = k*k + (k+1)*(k+1)
        max_gold = 0
        for x in range(n):
            for y in range(n):
                gold_count = 0
                for i in range(-k, k+1):
                    for j in range(-k, k+1):
                        if abs(i) + abs(j) <= k and 0 <= x+i < n and 0 <= y+j < n:
                            gold_count += grid[x+i][y+j]
                if gold_count * m >= cost:
                    max_gold = max(max_gold, gold_count)
        return max_gold

    # 가장 큰 K 값부터 시작하여 가장 많은 금을 채굴할 수 있는 경우를 찾음
    for k in range(n, -1, -1):
        result = count_gold_and_cost(k)
        if result > 0:
            return result
    return 0

print(max_gold_mining(n, m, board))