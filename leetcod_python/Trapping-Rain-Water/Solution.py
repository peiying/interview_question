class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        max_val = A[0]
        left = [A[0]]
        for i in xrange(1,len(A)):
            max_val = max(max_val, A[i])
            left.append(max_val)
        max_val = A[-1]
        right = [A[-1]]
        for i in xrange(len(A) - 2, -1, -1):
            max_val = max(max_val, A[i])
            right.insert(0, max_val)
        res = 0
        for i in xrange(len(A)):
            t = min(left[i], right[i])
            res += t - A[i]
        return res
            
