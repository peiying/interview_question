class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1 + dp[i - 1][j]
        res = 0
        for row in dp:
            res = max(res, self.largestRectangleArea(row))
        return res
        
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        i = 0
        maxArea = 0
        while i < len(height):
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                h = height[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
        return maxArea
