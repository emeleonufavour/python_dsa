# Definition for singly-linked list.
from typing import Optional


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

    def max_node(self):
        """Find the maximum number in a Linkedlist"""
        if self.head is None:
            return
        current_node = self.head
        max = self.head.val
        while current_node:
            if (max < current_node.val):
                max = current_node.val
            current_node = current_node.next
        print(f'Maximum no is {max}')

    def min_node(self):
        """Find the minimum number in a Linkedlist"""
        if self.head is None:
            return
        current_node = self.head
        min = self.head.val
        while current_node:
            if (min > current_node.val):
                min = current_node.val
            current_node = current_node.next
        print(f'Minimum no is {min}')

    def delete_node(self, key):
        """"Delete a Node from the Linkedlist"""
        current_node = self.head
        if current_node and current_node.val == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.val != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def print_list(self):
        """Print Linkedlist"""
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


class ListNode:
    """Node for LinkedList class"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_node(head: Optional[ListNode]):
    """Print all nodes"""
    if head is None:
        return
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next


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


def nodes_count(head: Optional[ListNode]) -> int:
    if head is None:
        return 0
    current_node = head
    count = 0
    while current_node:
        count = count + 1
        current_node = current_node.next


def delete_node(head: Optional[ListNode], key):
    """"Delete a Node from the Linkedlist"""
    current_node = head
    if current_node and current_node.val == key:
        print("Node to delete is head")
        head = current_node.next
        current_node = None
        print("List after deletion from head-> ")
        print_node(head)
        print("________")
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
    """Leetcode solution"""

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        # Find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge two lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # print("Printing all nodes....")
    # print_node(node1)
    # print("________")
    sol = Solution()
    sol.reorderList(node1)
