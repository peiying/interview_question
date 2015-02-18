class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        max_val = A[0]
        min_val = A[0]
        res = A[0]
        for i in range(1, len(A)):
            mx = max_val
            mn = min_val
            min_val = min(min(A[i], mx * A[i]), mn * A[i])
            max_val = max(max(A[i], mx * A[i]), mn * A[i])
            res = max(res, max_val)
        return res
        
