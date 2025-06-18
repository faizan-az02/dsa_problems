def find_max_fish(grid):

    m, n = len(grid), len(grid[0])

    visited = [[False] * n for _ in range(m)]

    def dfs(r, c):

        if r < 0 or r >= m or c < 0 or c >= n:

            return 0
        
        if visited[r][c] or grid[r][c] == 0:

            return 0
        
        visited[r][c] = True

        fish = grid[r][c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            fish += dfs(r + dr, c + dc)

        return fish

    max_fish = 0

    for r in range(m):

        for c in range(n):

            if grid[r][c] > 0 and not visited[r][c]:

                max_fish = max(max_fish, dfs(r, c))

    return max_fish

# Example usage:
if __name__ == "__main__":
    grid = [
        [0, 1, 2, 0],
        [3, 0, 4, 5],
        [0, 6, 0, 7],
        [8, 0, 9, 0]
    ]
    print(find_max_fish(grid))