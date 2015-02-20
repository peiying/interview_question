class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        
        x = 0
        y = 0
        while m > 0 and n > 0:
            if m == 1:
                for i in range(n):
                    res.append(matrix[x][y])
                    y += 1
                return res
            elif n == 1:
                for i in range(m):
                    res.append(matrix[x][y])
                    x += 1
                return res
            for i in range(n - 1):
                res.append(matrix[x][y])
                y += 1
            for i in range(m - 1):
                res.append(matrix[x][y])
                x += 1
            for i in range(n - 1):
                res.append(matrix[x][y])
                y -= 1
            for i in range(m - 1):
                res.append(matrix[x][y])
                x -= 1
            m -= 2
            n -= 2
            x += 1
            y += 1
        return res
                
            
        
