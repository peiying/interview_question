# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        stack = []
        curNode = root
        while stack or curNode is not None:
            if curNode is not None:
                stack.append(curNode)
                curNode = curNode.left
            else:
                t = stack.pop()
                res.append(t.val)
                curNode = t.right
        return res
