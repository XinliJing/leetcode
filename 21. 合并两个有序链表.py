# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1.val > l2.val:
        #     l = l2
        #     l2 = l2.next
        # else:
        #     l = l1
        #     l1 = l1.next
        # head = l
        l = ListNode(-1)
        head = l
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                l.next = l2
                l2 = l2.next
            else:
                l.next = l1
                l1 = l1.next
            l = l.next
        if l1 is None:
            l.next = l2
        else:
            l.next = l1
        return head.next
