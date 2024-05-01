from leetcode.reorder_list import ListNode


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
