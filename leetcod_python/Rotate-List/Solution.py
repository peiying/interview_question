# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        len = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            len += 1
        cur.next = head
        k = len - k % len
        pre = cur
        while k > 0:
            pre = pre.next
            k -= 1
        head = pre.next
        pre.next = None
        return head
            
