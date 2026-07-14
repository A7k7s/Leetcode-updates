# Last updated: 7/14/2026, 2:05:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        temp=head
        while(temp != None and curr != None):
            prev=temp.val
            if temp.next != None and temp.val==temp.next.val :
                while( temp != None and temp.val==prev):
                    temp=temp.next
                curr.next=temp
            else:
                temp=temp.next
                curr=curr.next
        return dummy.next