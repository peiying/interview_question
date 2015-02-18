class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif mid > 0 and A[mid] > target and A[mid - 1] < target:
                return mid
            elif mid < len(A) - 1 and A[mid] < target and A[mid + 1] > target:
                return mid + 1
            elif target < A[0]:
                return 0
            elif target > A[-1]:
                return len(A)
            elif A[mid] > target:
                end = mid - 1
            elif A[mid] < target:
                start = mid + 1
            
        
