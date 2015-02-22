#hash存char与对应的idx值
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        d = {}
        i = 0
        res = 0
        for j in xrange(len(s)):
            if s[j] in d and d[s[j]] >= i:
                i = d[s[j]] + 1
            d[s[j]] = j
            res = max(res, j - i + 1)
        return res
