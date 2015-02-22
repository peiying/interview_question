class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in xrange(len(A)):
            res = res ^ A[i]
        return res
        
