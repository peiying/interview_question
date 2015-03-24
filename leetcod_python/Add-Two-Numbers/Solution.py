# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while cur1 != None and cur2 != None:
            cur.next = ListNode((cur1.val + cur2.val + carry) % 10)
            carry = (cur1.val + cur2.val + carry) / 10
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next
        while cur1 != None:
            cur.next = ListNode((cur1.val + carry) % 10)
            carry = (cur1.val + carry) / 10
            cur1 = cur1.next
            cur = cur.next
        while cur2 != None:
            cur.next = ListNode((cur2.val + carry) % 10)
            carry = (cur2.val + carry) / 10
            cur2 = cur2.next
            cur = cur.next
        if carry == 1:
            cur.next = ListNode(1)
        return dummy.next
        
