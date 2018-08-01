# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        q = head.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p
    
        # 大佬的答案
        # prev = None
        # curr = head
        # while curr:
        #     nextTemp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextTemp
        # return prev
