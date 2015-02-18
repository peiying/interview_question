class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        t = [[1] * n] * m
        for i in range(1,m):
            for j in range(1,n):
                t[i][j] = t[i - 1][j] + t[i][j - 1]
        return t[m - 1][n -1]
        
