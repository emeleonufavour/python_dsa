# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        # Reverse the original linked list
        reversed_head = self.reverseList(head)
        
        # Double the reversed linked list
        carry = 0
        current = reversed_head
        while current is not None:
            # Multiply the current node's value by 2 and add the carry
            new_val = current.val * 2 + carry
            current.val = new_val % 10
            carry = new_val // 10
            if current.next is None and carry > 0:
                current.next = ListNode(carry)
                break
            current = current.next
        
        # Reverse the doubled linked list again
        doubled_head = self.reverseList(reversed_head)
        
        return doubled_head
        
            
        
        
if __name__ == "__main__":
    a = ListNode(9)
    b = ListNode(9)
    c = ListNode(9)

    
    a.next = b
    b.next = c

    sol = Solution()
    result = sol.doubleIt(a)
    current = result
    while current is not None:
        print(f"{current.val}")
        current = current.next
    # print(result)