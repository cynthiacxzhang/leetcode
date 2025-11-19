class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Reverse the rest of the list
    new_head = reverse_list(head.next)
    
    # Rewire the pointers
    head.next.next = head
    head.next = None
    
    return new_head
