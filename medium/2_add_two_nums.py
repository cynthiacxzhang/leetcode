# Add two numbers

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # new list
        dummy = ListNode(0)
        curr = dummy

        carry = 0

        # traversal and sum
        # loop condition: if either list still exists
        # or if there's a carry still pending
        while l1 or l2 or carry:

            # if one list "ends", treat node as 0
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            # calculate value of new node
            total = a + b + carry
            digit = total % 10
            carry = total // 10

            # instantiate new LL node with value
            new_node = ListNode(digit)
            curr.next = new_node # append to list

            # move forwards in all lists if l1/l2 is not None
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            curr = curr.next
        
        # adding carry if it still exists after full traversal
        if carry != 0:
            new_node = ListNode(carry)
            curr.next = new_node
        
        
        # no need to reverse
        return dummy.next

            
            

        
        