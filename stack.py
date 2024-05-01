
class Stack:
    """Class to generate Stack instance"""

    def __init__(self) -> None:
        self.stack = []

    def push(self, element) -> None:
        """Append an item to the stack"""
        self.stack.append(element)

    def pop(self):
        """Remove item from Stack"""
        return self.stack.pop()

    def peek(self):
        """"Look at the an item in the Stack"""
        return self.stack[-1]

    def length(self):
        """Returns length of stack"""
        return len(self.stack)


class Queue:
    """Class to generate Queue data structure"""

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, element):
        """Add item to the queue"""
        self.queue.append(element)

    def dequeue(self):
        """"Remove item from the queue"""
        self.queue.remove(0)

    def read(self):
        """"Read the top item in the queue"""
        return self.queue[0]


def reverse_string(string):
    """Reverse a string with Stack"""
    stack = Stack()
    reversed_string = []
    for i in list(string):
        stack.push(i)

    for i in range(stack.length()):
        reversed_string.append(stack.pop())

    return ''.join(reversed_string)


letters = reverse_string("ABCDE")
print(letters)
