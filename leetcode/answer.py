# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        """Add a node to the Linkedlist"""
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


def max_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Find the maximum number in a Linkedlist"""
    if head is None:
        return
    current_node = head
    max = head.val
    while current_node:
        if (max < current_node.val):
            max = current_node.val
        current_node = current_node.next

    return ListNode(max)


def min_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Find the minimum number in a Linkedlist"""
    if head is None:
        return
    current_node = head
    min = head.val
    while current_node:
        if (min > current_node.val):
            min = current_node.val
        current_node = current_node.next

    return ListNode(min)


def delete_node(head: Optional[ListNode], key):
    """"Delete a Node from the Linkedlist"""
    current_node = head
    if current_node and current_node.val == key:
        head = current_node.next
        current_node = None
        return head
    else:
        prev = None
        while current_node and current_node.val != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    return head


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        # Function to reverse the second half of the linked list
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Function to merge two linked lists
        def merge_lists(list1, list2):
            while list1 and list2:
                next1 = list1.next
                next2 = list2.next
                list1.next = list2
                list1 = next1
                list2.next = list1
                list2 = next2

        # Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = reverse_list(slow)

        # Merge the two halves of the linked list
        merge_lists(head, second_half)


def print_node(head: Optional[ListNode]):
    """Print all nodes"""
    if head is None:
        return
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    sol = Solution()
    sol.reorderList(node1)


# correct solution
class Solution2:
    def reverse(self, head):
        if not head:
            return None
        prev = None
        curr = head
        nextNode = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def merge(self, list1, list2):
        while list2:
            nextNode = list1.next
            list1.next = list2
            list1 = list2
            list2 = nextNode

    def reorderList(self, head):
        if not head or not head.next:
            return
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        list1 = head
        list2 = self.reverse(slow)
        self.merge(list1, list2)
