# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        while l1 != None:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2 != None:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next
            
            
