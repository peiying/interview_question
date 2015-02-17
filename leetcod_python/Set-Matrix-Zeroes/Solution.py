class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row_zero = False
        col_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_zero = True
                    if j == 0:
                        col_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if row_zero:
            for i in range(n):
                matrix[0][i] = 0
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
        
