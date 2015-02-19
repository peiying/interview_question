#搞了很久，还是可以用java的iterator思路
#可以用 + 来进行深copy
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
  def subsets(self, S):
      S.sort()
      res = [[]]
      for i in range(len(S)):
          for j in range(len(res)):
              res.append(res[j] + [S[i]])
      return res
