#define first and last

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n / 2):
            first = i
            last = n - 1 - i
            for j in range(first, last):
                offset = j - first
                temp = matrix[first][j]
                matrix[first][j] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[j][last]
                matrix[j][last] = temp
        return matrix
                
