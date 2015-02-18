# lc cleancode 上的答案过不了case （1，3，3）
#对于这种不是rotated array的case，先比较start和end，如果start < end 直接go left
#其他情况一样，与start或者end比较都可，如果出现dup， start++
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = 0
        r = len(num) - 1
        while l < r:
            m = l + (r - l) / 2
            if num[l] < num[r]:
                r = m
            elif num[m] > num[l]:
                l = m + 1
            elif num[m] < num[l]:
                r = m
            else:
                l += 1
        return num[l]
        
