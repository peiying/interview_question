# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next != None:
            fast = fast.next
            if fast.next == None:
                break
            slow = slow.next
            fast = fast.next
        l = head
        r = slow.next
        slow.next = None
        pre = r
        cur = r.next
        pre.next = None
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        if cur == None:
            r = pre
        else:
            r = cur
        p = l
        q = r
        while p != None and q != None:
            pNext = p.next
            qNext = q.next
            p.next = q
            q.next = pNext
            p = pNext
            q = qNext
        return l
            
