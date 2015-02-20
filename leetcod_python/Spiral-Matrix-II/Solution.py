class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        x = 0
        y = 0
        count = 1
        while n > 0:
            if n == 1:
                matrix[x][y] = count
                return matrix
            for i in range(n - 1):
                matrix[x][y] = count
                y += 1
                count += 1
            for i in range(n - 1):
                matrix[x][y] = count
                x += 1
                count += 1
            for i in range(n - 1):
                matrix[x][y] = count
                y -= 1
                count += 1
            for i in range(n - 1):
                matrix[x][y] = count
                x -= 1
                count += 1
            n -= 2
            x += 1
            y += 1
        return matrix
                
