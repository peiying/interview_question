class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if (m + n) % 2 == 1:
            return self.helper(A, B, 0, m - 1, 0, n - 1, (m + n) / 2)
        else:
            t1 = self.helper(A, B, 0, m - 1, 0, n - 1, (m + n) / 2)
            t2 = self.helper(A, B, 0, m - 1, 0, n - 1, (m + n) / 2 - 1)
            return (t1 + t2) * 0.5
    def helper(self, A, B, startA, endA, startB, endB, k):
        lenA = endA - startA + 1
        lenB = endB - startB + 1
        if lenA == 0:
            return B[startB + k]
        if lenB == 0:
            return A[startA + k]
        if k == 0:
            return min(A[startA], B[startB])
        midA = lenA * k / (lenA + lenB)
        midB = k - midA - 1
        midA = midA + startA
        midB = midB + startB
        if A[midA] > B[midB]:
            k = k - (midB - startB + 1)
            endA = midA
            startB = midB + 1
        else:
            k = k - (midA - startA + 1)
            endB = midB
            startA = midA + 1
        return self.helper(A, B, startA, endA, startB, endB, k)
        
        
        
