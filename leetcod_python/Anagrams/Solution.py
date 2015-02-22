#最后结果用extend 相当于addAll
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        res = []
        for str in strs:
            key = ''.join(sorted(str))
            if key in d:
                d[key].append(str)
            else:
                d[key] = [str]
        for i in d:
            if len(d[i]) > 1:
                res.extend(d[i]) 
        return res
