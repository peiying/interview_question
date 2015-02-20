class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        left = 0
        right = len(A) - 1
        mid = 0
        while mid <= right:
            if A[mid] == 0:
                A[left], A[mid] = A[mid], A[left]
                left += 1
                mid += 1
            elif A[mid] == 1:
                mid += 1
            else:
                A[mid], A[right] = A[right], A[mid]
                right -= 1
        
