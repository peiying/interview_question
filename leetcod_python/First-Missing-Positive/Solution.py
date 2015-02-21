class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in xrange(len(A)):
            t = A[i]
            while t > 0 and t < len(A) + 1 and t != A[t - 1] and t != i + 1:
                temp = A[t - 1]
                A[t - 1] = t
                t = temp
            A[i] = t
        for i in xrange(len(A)):
            if i + 1 != A[i]:
                return i + 1
        return len(A) + 1
