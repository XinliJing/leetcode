# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = n
        nodeOne = head
        nodeTwo = head
        for i in range(n):
            nodeOne = nodeOne.next
        if nodeOne == None:
            return head.next
        while nodeOne.next != None:
            nodeOne = nodeOne.next
            nodeTwo = nodeTwo.next
        nodeTwo.next = nodeTwo.next.next
        return head
