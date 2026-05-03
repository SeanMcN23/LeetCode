# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first= head
        second=None

        while first is not None:
            temp=first
            first=first.next
            temp.next=second
            second=temp
        return second
            
