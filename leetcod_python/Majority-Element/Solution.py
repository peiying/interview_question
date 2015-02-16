class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        res = num[0]
        count = 1
        for i in range(1,len(num)):
            if count == 0:
                res = num[i]
                count += 1
            elif res == num[i]:
                count += 1
            elif res != num[i]:
                count -= 1
        return res
