# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """

        slow,fast=head,head.next

        # now we need to know both halfs first

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # now lets reverse the second half

        second=slow.next
        # disconnect the 2 halfs and need prev
        prev=slow.next=None

        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        
        # now we need to merge the 2 halfs into this reorder list

        first,second= head, prev

        while second:
            tmp1,tmp2= first.next,second.next
            first.next=second
            second.next=tmp1
            first,second= tmp1,tmp2

        

        