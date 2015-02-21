class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        res = 0
        s = set()
        for e in num:
            s.add(e)
        for e in num:
            count = 1
            c = e
            while c - 1 in s:
                count += 1
                c -= 1
                s.remove(c)
            c = e
            while c + 1 in s:
                count += 1
                c += 1
                s.remove(c)
            res = max(res, count)
        return res
