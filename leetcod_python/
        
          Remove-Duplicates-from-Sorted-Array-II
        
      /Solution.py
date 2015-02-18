class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        count = 0
        j = 1
        for i in range(1, len(A)):
            if(A[i] == A[i - 1]):
                count += 1
                if(count <= 1):
                    A[j] = A[i]
                    j += 1
            else:
                A[j] = A[i]
                j += 1
                count = 0
        return j
