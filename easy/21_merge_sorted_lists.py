# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # heads of both lists for traversal
        curr1 = list1
        curr2 = list2

        # dummy vars for merged list
        # tmp node to start everything so that new head = tmp.next
        tmp = ListNode(-1) 
        tail = tmp # current end of list is that single node

        # while both lists aren't empty
        # and because if one finished, exit and append the rest of the other
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1 
                tail = tail.next
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next

        # append whichever list isn't empty to the end of the built list 
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        return tmp.next
            
            
            





        