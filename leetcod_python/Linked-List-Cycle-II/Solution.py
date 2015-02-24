# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:
            return None
        slow = head
        fast = head
        while True:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                break
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
