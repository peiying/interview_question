#while left < right and num[left] == num[left - 1]:
#                            left += 1
#                        while left < right and num[right] == num[right + 1]:
#                            right -= 1
# This part is important. Using previous one can not AC
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        n = len(num)
        res = []
        num.sort()
        for i in range(n - 3):
            if i > 0 and num[i] == num[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and num[j] == num[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum = num[i] + num[j] + num[left] + num[right]
                    if sum == target:
                        res.append([num[i], num[j], num[left], num[right]])
                        left += 1
                        right -= 1
                        while left < right and num[left] == num[left - 1]:
                            left += 1
                        while left < right and num[right] == num[right + 1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
