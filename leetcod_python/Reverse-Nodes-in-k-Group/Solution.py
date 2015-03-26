# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy
        count = 0
        while cur != None:
            count += 1
            end = cur.next
            if count == k:
                pre = self.reverse(pre, end)
                count = 0
            cur = end
        return dummy.next
        
    def reverse(self, pre, end):
        if pre is None or pre.next is None:
            return pre
        cur = pre.next
        while cur.next != end:
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return cur
        
