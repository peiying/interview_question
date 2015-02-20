class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        max_len = 0
        for i in range(len(A)):
            if max_len >= len(A) - 1:
                return True
            if max_len >= i:
                max_len = max(max_len, i + A[i])
            else:
                return False
        return False
        
