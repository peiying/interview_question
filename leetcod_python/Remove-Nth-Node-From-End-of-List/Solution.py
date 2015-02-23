# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while n > 0:
            cur = cur.next
            n -= 1
        p = dummy
        while cur.next != None:
            cur = cur.next
            p = p.next
        if p.next != None:
            p.next = p.next.next
        else:
            p.next = None
        return dummy.next
