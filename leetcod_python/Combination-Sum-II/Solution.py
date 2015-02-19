class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        list = []
        res = []
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
                if prev == None or prev != c:
                    list.append(c)
                    self.helper(candidates[i + 1:], target - c, list, res)
                    list.pop()
                prev = c
                
        
           
