class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        n = len(num)
        res = num[0] + num[1] + num[2]
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                sum = num[i] + num[l] + num[r]
                if abs(target - sum) < abs(target - res):
                    res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return res
                
        
