# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # use set to track visited nodes
        # basially equivalent to check duplicates

        seen = set()
        curr = head

        while curr and curr.next != None:
            if curr in seen:
                return True
            else:
                seen.add(curr)
            curr = curr.next
        return False
