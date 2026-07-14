# Last updated: 7/14/2026, 2:04:33 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        one=head
        two=head
        while two and two.next:
            one=one.next
            two=two.next.next
            if two==one:
                return True
        return False
        