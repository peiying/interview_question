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
        p = head
        q = p.next
        while q != None:
            if p.val == q.val:
                p.next = p.next.next
                q = p.next
            else:
                p = p.next
                q = q.next
        return head
        
