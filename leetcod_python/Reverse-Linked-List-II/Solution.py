# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        t = m - 1
        while t > 0:
            cur = cur.next
            t -= 1
        k = n - m
        pre = cur
        cur = pre.next
        while cur.next != None and k > 0:
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
            k -= 1
        return dummy.next
