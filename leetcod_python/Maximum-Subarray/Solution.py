class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        res = A[0]
        curSum = A[0]
        for i in range(1,len(A)):
            if curSum < 0:
                curSum = 0
            curSum += A[i]
            res = max(res, curSum)
        return res
            
