# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       # this will need a dummy variable, saw it alrdy
        dummy= ListNode(None)
        curr=dummy

        if list1 == None and list2 == None:
            return None
        elif list2 == None:
            return list1
        elif list1 == None:
            return list2


        if list1.val > list2.val:
            dummy.next=list2
            list2 = list2.next
        else:
            dummy.next=list1
            list1=list1.next
        curr=curr.next
       
        while list1 != None and list2 != None:

            if list1.val > list2.val:
                curr.next=list2
                list2=list2.next
             
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next
        
        if list1 is not None:
            curr.next=list1
        elif list2 is not None:
            curr.next=list2
        
        return dummy.next




    

        