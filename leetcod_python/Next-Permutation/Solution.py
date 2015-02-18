class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        l = -1
        r = -1
        for i in range(n - 1):
            if num[i] < num[i + 1]:
                l = i
        if l != -1:
            for i in range(n):
                if num[i] > num[l]:
                    r = i
            num[l], num[r] = num[r], num[l]
        left = l + 1
        right = n - 1
        while left < right:
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1
        return num
