class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            return res
        for i in range(2,numRows):
            cur = []
            for j in range(i + 1):
                if j == 0:
                    cur.append(1)
                elif j == i:
                    cur.append(1)
                else:
                    c = res[i - 1][j - 1] + res[i - 1][j]
                    cur.append(c)
            res.append(cur)
        return res
        
