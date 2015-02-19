#iterator版本，code is clean，runtime is less
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        res = [[]]
        prev = 0
        for i in range(len(S)):
            cur = 0
            if i > 0 and S[i] == S[i - 1]:
                cur = prev
            size = len(res)
            for j in range(cur,size):
                res.append(res[j] + [S[i]])
            prev = size
        return res
        
