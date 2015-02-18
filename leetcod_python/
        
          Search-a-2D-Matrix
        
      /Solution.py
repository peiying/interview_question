class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return False
        start = 0
        end = m * n - 1
        while start <= end:
            mid = start + (end - start) / 2
            i = mid / n
            j = mid % n
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                end = mid - 1
            else:
                start = mid + 1
        return False
        
