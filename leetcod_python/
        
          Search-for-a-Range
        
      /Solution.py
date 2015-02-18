class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                i = mid
                while i >= 0 and A[i] == target:
                    i -= 1
                first = i + 1
                i = mid
                while i < len(A) and A[i] == target:
                    i += 1
                second = i - 1
                return [first, second]
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]
        
        
