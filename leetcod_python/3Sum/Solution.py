class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        res = []
        n = len(num)
        num.sort()
        for i in range(n - 2):
            if i > 0 and num[i] == num[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if l > i + 1 and num[l] == num[l - 1]:
                    l += 1
                    continue
                if r < n - 1 and num[r] == num[r + 1]:
                    r -= 1
                    continue
                sum = num[i] + num[l] + num[r]
                if sum == 0:
                    res.append([num[i], num[l], num[r]])
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res
                    
        
