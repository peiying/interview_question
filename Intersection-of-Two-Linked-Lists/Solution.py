# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        cur = headA
        lenA = 0
        while cur != None:
            lenA += 1
            cur = cur.next
        cur = headB
        lenB = 0
        while cur != None:
            lenB += 1
            cur = cur.next
        curA = headA
        curB = headB
        if lenA >= lenB:
            d = lenA - lenB
            while d > 0:
                curA = curA.next
                d -= 1
        else:
            d = lenB - lenA
            while d > 0:
                curB = curB.next
                d -= 1
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
        
