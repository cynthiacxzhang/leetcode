# 21 Merge Two Sorted Linked Lists

"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Note: ListNode is a class that initializes a node object with a self.val and a self.next
        # - self.val is initializes in the parameter (e.g. if a = ListNode(1), a.val = 1
        # - self.next is by default pointing to None (if there's no next items in the list)

        # Create a dummy that acts like the start of the linked list
        dummy = ListNode(-1)    # dummy = [-1]
        current = dummy         # current points to the same node as dummy

        # Essentially we're constructing the list starting from current
        # - current and dummy point to the same value
        # - current is being updated, whereas dummy stays pointed to the first value in the new list
        # - return dummy.next at the end since dummy is the value before the first merged list value


        # For unempty lists, loop through both
        while list1 and list2: 
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next  # moving down list if value is retrieved
            else: 
                current.next = list2
                list2 = list2.next  # moving down list if value is retrieved
            current = current.next  # setting current value as whichever list val is smaller

        # When one of the lists become empty
        # - append the rest of the other list onto the end of the merged one
        if list1:
            current.next = list1    # if list1 still has values
        else:
            current.next = list2    # if list1 is the empty list, append the rest of list2

        return dummy.next



        