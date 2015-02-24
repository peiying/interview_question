# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        cur = head
        cnt = 0
        while cur != None:
            cur = cur.next
            cnt += 1
        root = self.helper([head], 0, cnt - 1)
        return root
    def helper(self, head, left, right):
        if left > right:
            return None
        mid = left + (right - left) / 2
        left = self.helper(head,left, mid - 1)
        root = TreeNode(head[0].val)
        head[0] = head[0].next
        right = self.helper(head,mid + 1, right)
        root.left = left
        root.right = right
        return root
        
