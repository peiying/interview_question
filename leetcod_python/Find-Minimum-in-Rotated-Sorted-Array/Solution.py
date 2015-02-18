#mid 要与 end 比较： 如果与start比较，过不了case （3，1）
#注意 go left时候 inclusive mid
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        r = len(num) - 1
        while l < r:
            mid = l + (r - l) / 2
            if num[mid] > num[r]:
                l = mid + 1
            else:
                r = mid
        return num[l]
            
