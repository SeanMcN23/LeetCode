# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myHead=head
        prev= None

        while myHead:
            temp=myHead.next
            myHead.next=prev
            prev=myHead
            myHead=temp
        return prev

            
