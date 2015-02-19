class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        list = []
        res = []
        candidates.sort()
        self.helper(candidates, target, list, res)
        return res
        
    def helper(self, candidates, target, list, res):
        if target < 0:
            return
        elif target == 0:
            res.append(list[:])
        else:
            prev = None
            for i, c in enumerate(candidates):
                if prev is None or prev != c:
                    list.append(c)
                    self.helper(candidates[i:], target - c, list, res)
                    list.pop()
                prev = c
        
        
