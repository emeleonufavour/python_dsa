# Definition for singly-linked list.
from typing import Optional


# Define a class to represent a single node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node in the linked list

# Define a class to solve the problem
class Solution:
    # Function to reverse a linked list
    def reverseLinkedList(self, head):
        prev = None  # Initialize a variable to store the previous node
        current = head  # Start from the head of the original list
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the pointer to the previous node
            prev = current  # Move to the next node
            current = next_node  # Move to the next node
        return prev  # Return the new head of the reversed list

    # Function to delete nodes with greater values to the right
    def deleteNodes(self, head):
        max_val = float('-inf')  # Initialize a variable to store the maximum value encountered so far
        dummy = ListNode(0)  # Create a dummy node to handle edge cases
        dummy.next = head  # Link the dummy node to the head of the list
        current = dummy  # Start from the dummy node

        while current.next:
            if current.next.val < max_val:  # If the value of the next node is less than the maximum value
                current.next = current.next.next  # Delete the next node by skipping it
            else:
                max_val = current.next.val  # Update the maximum value
                current = current.next  # Move to the next node

        return dummy.next  # Return the head of the modified list

    # Function to remove nodes with greater values to the right
    def removeNodes(self, head):
        if not head:
            return None  # If the list is empty, return None

        reversed_head = self.reverseLinkedList(head)  # Reverse the original list
        modified_head = self.deleteNodes(reversed_head)  # Delete nodes with greater values
        return self.reverseLinkedList(modified_head)  # Reverse the modified list again
            


if __name__ == "__main__":
    a = ListNode(5)
    b = ListNode(2)
    c = ListNode(13)
    d = ListNode(3)
    e = ListNode(8)
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    sol = Solution()
    new_head = sol.removeNodes(a)
    # print(result)
    current = new_head
    while current is not None:
        print(current.val)
        current = current.next