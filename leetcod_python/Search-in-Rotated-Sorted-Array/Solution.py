# completely same with ii which contains duplicate element
# for the case [1] 0
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = start + (end - start)
            if A[mid] == target:
                return mid
            elif A[mid] < A[end]:
                if target > A[mid] and target < A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif A[mid] > A[end]:
                if target < A[mid] and target > A[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1
        return -1
        
