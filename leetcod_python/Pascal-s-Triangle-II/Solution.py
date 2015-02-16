class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = [1 for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                j = i - j
                res[j] += res[j - 1]
        return res
