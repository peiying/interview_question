class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        i = 0
        j = 0
        while j < len(A):
            if A[i] == A[j]:
                j += 1
            else:
                i += 1
                A[i] = A[j]
                j += 1
        return i + 1
        
