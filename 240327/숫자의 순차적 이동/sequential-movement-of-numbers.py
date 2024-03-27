import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def move_numbers(n, m, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def find_position(number):
        for x in range(n):
            for y in range(n):
                if grid[x][y] == number:
                    return x, y
        return None, None

    for _ in range(m):
        for number in range(1, n * n + 1):
            x, y = find_position(number)
            max_val = -1
            max_pos = (x, y)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] > max_val:
                        max_val = grid[nx][ny]
                        max_pos = (nx, ny)
            # 교환
            grid[x][y], grid[max_pos[0]][max_pos[1]] = grid[max_pos[0]][max_pos[1]], grid[x][y]

    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

print_grid(move_numbers(n, m, board))