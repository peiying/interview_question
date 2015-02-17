class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        t = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    t[i][j] = grid[i][j]
                elif i == 0:
                    t[i][j] = grid[i][j] + t[i][j - 1]
                elif j == 0:
                    t[i][j] = grid[i][j] + t[i - 1][j]
                else:
                    t[i][j] = grid[i][j] + min(t[i][j - 1], t[i - 1][j])
        return t[m - 1][n - 1]
        
