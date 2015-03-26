# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        l1 = ListNode(0)
        l2 = ListNode(0)
        left = l1
        right = l2
        cur = head
        while cur != None:
            if cur.val < x:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
        right.next = None
        left.next = l2.next
        return l1.next
        
