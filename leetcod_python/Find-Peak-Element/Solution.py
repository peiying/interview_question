class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        start = 0
        end = len(num) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if (mid == 0 or num[mid] > num[mid - 1]) and (mid == end or num[mid] > num[mid + 1]):
                return mid
            elif (mid > 0 and num[mid] > num[mid - 1]) or (mid < end and num[mid] < num[mid + 1]):
                start = mid + 1
            else:
                end = mid - 1
        
