# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        p = head
        q = head.next
        r = head.next
        if r.next is None:
            if p.val != q.val:
                return False
            else:
                return True
        p.next = None
        while r.next is not None and r.next.next is not None:
            r = r.next.next
            temp = p
            p = q
            q = q.next
            p.next = temp
        if r.next is not None:
            q = q.next
        while p is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

        # 学习学习
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         node = None
#         while slow:
#             slnext = slow.next
#             slow.next = node
#             node = slow
#             slow = slnext
            
#         while node and head:
#             if node.val != head.val:
#                 return False
#             node = node.next
#             head = head.next
#         return True
