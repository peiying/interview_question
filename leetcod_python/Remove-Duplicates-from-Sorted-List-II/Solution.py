# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        next = cur.next
        while next != None:
            if cur.val == next.val:
                while cur.val == next.val:
                    next = next.next
                    if next == None:
                        pre.next = None
                        return dummy.next
                pre.next = next
                cur = next
                next = cur.next
            else:
                pre = pre.next
                cur = cur.next
                next = next.next
        return dummy.next
