# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        map = {}
        p = head
        while p != None:
            map[p] = RandomListNode(p.label)
            p = p.next
        dummy = RandomListNode(0)
        p = head
        q = dummy
        while p != None:
            temp = map[p]
            if p.random == None:
                temp.random == None
            else:
                temp.random = map[p.random]
            q.next = temp
            q = q.next
            p = p.next
        return dummy.next
