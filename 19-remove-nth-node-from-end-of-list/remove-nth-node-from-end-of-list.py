# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # im thinking if i reverse it, then count backwards with ocunter, then i can reverse the list again and boom, all done
        if head.next==None and n == 1:
            return None

        myHead=head

        # lets first swap the direction
        prev=None
        
        while myHead:
            tmp=myHead.next
            myHead.next=prev
            prev=myHead
            myHead=tmp
        
        prev2=myHead
        myHead2=prev
        counter=1
        while myHead2:
            if counter == n and n==1:
                prev2=myHead2
                myHead2=myHead2.next
                prev2.next=None
                prev=myHead2
                break

            if counter == n:
                tmp=myHead2.next
                prev2.next=tmp
                break
            prev2=myHead2
            myHead2=myHead2.next
            counter += 1
           
        while prev:
            tmp=prev.next
            prev.next=myHead
            myHead=prev
            prev=tmp
        return myHead
            
        
        