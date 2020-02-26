"""Contains code for StackADTs
CPE202
Project 1 Code Modified for use in Project 2

Author:
    John Wright
"""
from linked_list import Node
import linked_list


class StackLinked:
    """Stack using linked list
    Attributes:
        top (Node) : a linked list
        num_items (int) : number of items
    """

    def __init__(self, top=None, num_items=0):
        self.top = top
        self.num_items = num_items

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def is_empty(self):
        """If stack is empty returns true else false.
        Args:
            self (StackLinked): Linked List Stack
        Returns:
            (bool): Whether list is empty
        """
        if self.top is None:
            return True
        return False

    def push(self, item):
        """Pushes item to the Stack
        Args:
            self (StackLinked): Linked List Stack
        """
        self.top = linked_list.insert(self.top, item, self.num_items)
        self.num_items += 1

    def pop(self):
        """Pop an item from the stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): int popped from stack
        """
        if self.top is None:
            raise IndexError('')
        self.top, item = linked_list.pop(self.top, self.num_items-1)
        self.num_items -= 1
        return item

    def peek(self):
        """Returns the value at the top of the Stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): value on top of stack
        """
        if self.top is None:
            raise IndexError('')
        return linked_list.get(self.top, self.num_items-1)

    def size(self):
        """Returns the number of items in the Stack
        Args:
            self (StackArray): The Stack
        Returns:
            (int): num of items in stack
        """
        return self.num_items
