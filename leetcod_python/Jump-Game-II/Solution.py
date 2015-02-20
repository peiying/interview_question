class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        temp = 0
        max_len = 0
        step = 0
        for i in range(len(A)):
            if max_len >= len(A) - 1:
                break
            while i <= temp:
                max_len = max(max_len, i + A[i])
                i += 1
            step += 1
            temp = max_len
        return step
        
