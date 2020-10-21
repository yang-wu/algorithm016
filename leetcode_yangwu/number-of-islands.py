#200. 岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
